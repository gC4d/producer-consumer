import threading
import time
import queue

BASE_TIMEOUT = 0.5  
BUFFER_SIZE = 5
MAX_ITEMS = 15


class ProducerConsumer:
    
    def __init__(self, buffer_size=5, num_producers=2, num_consumers=2, max_items=10):
        self.buffer_size = buffer_size
        self.max_items = max_items
        
        self.buffer = queue.Queue(maxsize=buffer_size)
        
        self.items_produced = 0
        self.production_lock = threading.Lock()
        self.done = threading.Event()
        
    def producer(self, producer_id):
        """Produtor: gera itens e os coloca na fila"""
        
        while True:
            with self.production_lock:
                if self.items_produced >= self.max_items:
                    break
                
                item_id = self.items_produced + 1
                self.items_produced += 1
                
            item = f"Item-{item_id}"
            self.buffer.put(item)
            print(f"Producer {producer_id}: Added ({item})")
            
            time.sleep(1)
            
    def consumer(self, consumer_id):
        """Consumidor: pega itens da fila e os processa"""
        
        while not self.done.is_set() or not self.buffer.empty():
            try:
                item = self.buffer.get(timeout=BASE_TIMEOUT)
                
                print(f"Consumer {consumer_id}: Got ({item})")
                time.sleep(1)
                
                self.buffer.task_done()
                
            except queue.Empty:
                continue
    
    
def run():
    """"""
    simulation = ProducerConsumer(buffer_size=BUFFER_SIZE, max_items=MAX_ITEMS)
    
    producers = []
    for i in range(2): 
        thread = threading.Thread(target=simulation.producer, args=(i,))
        producers.append(thread)
        thread.start()
    
    consumers = []
    for i in range(2):
        thread = threading.Thread(target=simulation.consumer, args=(i,))
        consumers.append(thread)
        thread.daemon = True  
        thread.start()
    
    for thread in producers:
        thread.join()
    
    simulation.buffer.join()
    
    simulation.done.set()
    
    

if __name__ == "__main__":
    print("Producer-Consumer Problem!")
    print(f"Buffer size: {BUFFER_SIZE}, Max items: {MAX_ITEMS}\n")
    
    run()
    
    print("\nSimulation completed!")
