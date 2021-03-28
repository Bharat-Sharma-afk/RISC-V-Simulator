#memory access

#create memory class
class mem:
  #create dictionary~CPU Memory
  #dictionary <int,int/Byte> ~ <address,value>
  memory = {}
 
  #create following class variables:
  #code_start ~ text segment
  #data_start ~ data segment
  #data_stop 
  #stack_start ~ stack segment
  #heap_start ~ heap segment
  code_start=0
  data_start=0
  datat_stop=0
  stack_start=0
  heap_start=0
  
  #create following methods/functions
  #load_data,load_word,load_byte etc.
  def load_data():
  def load_word():
  def load_byte():
    
  #store_data,store_word,store_byte etc.
  def store_data():
  def store_word():
  def store_byte():
    
  #get_next_instruction
  def next_instruction():
  #get_data_at
  def get_data():
  #add_data_at
  def add_data():
  #show_memory
  def show_mem():
  

#create PC class
class PC:  
  #create following methods
  #add_PC
  #get_PC
  def add_PC():
  def get_PC():


#create Registers class:
class reg:  
  #create 32 registers
  regs=[[0 for i in range(32)] for i in range(32)] 
  
  #create following methods
  #load_from_register
  #store_to_register
  #print_register_value
  def load():
  def store():
  def print():
  
  
#create ... 

