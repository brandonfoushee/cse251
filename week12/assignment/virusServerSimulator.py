import json
import threading
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn

from virusApi import *

SLEEP = 1 # set this to 0.001 while you are testing, then turn it back to 1
MAX_GENERATIONS = 6


virus_names = ["".join(["COVID-", str(v)]) for v in range(500000)]

viruses = {}
families = {}

max_thread_count = 0
call_count = 0
thread_count = 0
lock = threading.Lock()
generations_created = 0
family_request_order = []
virus_uid = []
family_uid = []


def get_next_virus():
    return virus_names.pop(0)


# ----------------------------------------------------------------------------
def build_pandemic(gens):
    print(f'Building Pandemic ...')
    global viruses
    global families
    global virus_uid
    global family_uid

    viruses = {}
    families = {}

    def _create_family(generation):
        with lock:
            next_virus_id = virus_uid.pop(0)
            next_family_id = family_uid.pop(0)

        print(f'Generation: {generation}')
        print(f'next person / family: {next_virus_id} / {next_family_id}')
        if generation < 1:
            return

        virus1 = Virus(next_virus_id, get_next_virus())
        viruses[next_virus_id] = virus1
        with lock:
            next_virus_id = virus_uid.pop(0)

        virus2 = Virus(next_virus_id, get_next_virus())
        viruses[next_virus_id] = virus2
        with lock:
            next_virus_id = virus_uid.pop(0)

        family = Family(next_family_id, virus1.id, virus2.id, [])
        virus1.add_family(next_family_id)
        virus2.add_family(next_family_id)
        families[next_family_id] = family
        
        # always 2 offspring
        for i in range(2):
            offspring = Virus(next_virus_id, get_next_virus())
            viruses[next_virus_id] = offspring
            family.add_offspring(offspring.id)

        if generation > 1:
            # create parents and recursive calls
            virus1_parents = _create_family(generation - 1)
            virus1.add_parent(virus1_parents.id)
            virus1_parents.add_offspring(virus1.id)

            virus2_parents = _create_family(generation - 1)
            virus2.add_parent(virus2_parents.id)
            virus2_parents.add_offspring(virus2.id)

        # return the family that was created
        return family

    _create_family(gens)

    print(f'Number of viruses  : {len(viruses)}')
    print(f'Number of families: {len(families)}')


# ----------------------------------------------------------------------------
class Handler(BaseHTTPRequestHandler):

    def get_virus(self, id):
        global viruses
        if id in viruses:
            return viruses[id].get_dict()
        else:
            return None

    def get_family(self, id):
        global families
        if id in families:
            return families[id].get_dict()
        else:
            return None

    def do_GET(self):
        global thread_count
        global lock
        global max_thread_count
        global call_count
        global family_request_order
        global generations_created
        global start_family_id
        global virus_uid
        global family_uid

        with lock:
            thread_count += 1
            call_count += 1
            if thread_count > max_thread_count:
                max_thread_count = thread_count
            #print(f'Current: active threads / max count: {thread_count} / {max_thread_count}')

        #print('- ' * 35)
        print(f'Request: {self.path}')

        if SLEEP > 0:
            time.sleep(SLEEP)

        if 'start' in self.path:
            family_request_order = []
            parts = self.path.split('/')
            if len(parts) < 3:
                self.send_response(404)
                self.send_header("Content-type",  "application/json")
                self.end_headers()
                with lock:
                    thread_count -= 1
                return

            try:
                generations = int(parts[-1])
            except:
                generations = MAX_GENERATIONS

            output = f'Creating family pandemic with {generations} generations...'
            print(output)

            generations_created = generations
            build_pandemic(generations)

            json_data = '{"status":"OK"}'

        elif 'end' in self.path:
            print('#' * 80)

            print(f'Total number of viruses  : {len(viruses)}')
            print(f'Total number of families: {len(families)}')
            print(f'Number of generations   : {generations_created}')
            
            print('Families were requested in this order:')
            output = str(family_request_order)[1:-1]
            print(output)

            print(f'Total number of API calls: {call_count}')

            print(f'Maximum threads at one time: {max_thread_count}')
            
            json_data = '{"status":"OK"}'

            print('#' * 80)

        elif 'virus' in self.path or 'family' in self.path:
            parts = self.path.split('/')
            print('****************************')
            print(f'{parts=}')

            if len(parts) < 3:
                self.send_response(404)
                self.send_header("Content-type",  "application/json")
                self.end_headers()
                with lock:
                    thread_count -= 1
                return

            try:
                id = int(parts[-1])
            except:
                id = None

            if id == None:
                self.send_response(404)
                self.send_header("Content-type",  "application/json")
                self.end_headers()
                with lock:
                    thread_count -= 1
                return

            if 'virus' in self.path:
                data = self.get_virus(id)
            else:
                data = self.get_family(id)
                print(f'------- GET FAMILY ---- data={data}')
                family_request_order.append(int(parts[-1]))

            if data != None:
                json_data = json.dumps(data)
            else:
                json_data = None
                
        else: # BEGIN A NEW SIMULATION
           
            print('\n\n\n\n\n-----------------------')
            print('STARTING NEW SIMULATION')
            print('-----------------------\n')
            
            # create new uid each time start is called
            starting_family_id = 1000
            virus_uid = [i for i in range(1, 10000)]
            family_uid = [i for i in range(starting_family_id, 100000)]
            
            # start counters over
            max_thread_count = 1
            thread_count = 1
            call_count = 1
            
            data = {"start_family_id": starting_family_id} 
            json_data = json.dumps(data)

        if json_data == None:
            self.send_response(404)
            self.send_header("Content-type",  "application/json")
            self.end_headers()
        else:
            print('Sending:', json_data)

            self.send_response(200)
            self.send_header("Content-type",  "application/json")
            self.end_headers()
            self.wfile.write(bytes(json_data, "utf8"))

        with lock:
            thread_count -= 1


class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass


if __name__ == '__main__':
    # random.seed(101)

    # for id in people:
    #     print(people[id])
    # print('*' * 50)
    # for id in families:
    #     print(families[id])

    server = ThreadingSimpleServer((hostName, serverPort), Handler)
    print('Starting server, use <Ctrl-C> or <Command-C> to stop')
    server.serve_forever()
