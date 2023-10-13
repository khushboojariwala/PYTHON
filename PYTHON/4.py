"""
4-How memory is managed in Python?

    Memory management in Python is primarily handled by the Python memory manager. Python uses a combination of strategies to efficiently allocate and manage memory. Here are some key aspects of memory management in Python:
    
    Automatic Memory Management: 
    Python utilizes automatic memory management, which means developers do not need to explicitly allocate or deallocate memory as in languages like C or C++. Python automatically takes care of allocating and releasing memory as needed.
    
    Memory Allocation: 
    Python's memory manager allocates memory in two main parts:
    
        Heap: 
        The heap is where objects are stored. Python's memory manager keeps track of all objects in memory and is responsible for allocating and deallocating memory as needed.

        Stack: 
        The stack is used to manage function call frames and local variables. It keeps track of the execution context and is separate from the heap.
    
    Reference Counting: 
    Python uses reference counting as one of its memory management strategies. Each object has a reference count associated with it. When an object's reference count drops to zero, the memory occupied by that object is automatically released.
    
    Garbage Collection: 
    Python employs a cyclic garbage collector that deals with reference cycles. Reference cycles occur when objects reference each other, forming a closed loop, which can't be cleaned up by simple reference counting. The garbage collector identifies and cleans up these cycles, preventing memory leaks.
    
    Memory Pools: 
    Python uses a system of memory pools to efficiently allocate memory for small objects. These pools are divided into different size classes, and objects of a specific size are allocated from the appropriate pool.
    
    Memory Fragmentation: 
    Python's memory manager may suffer from fragmentation over time. The cyclic garbage collector helps mitigate this, but some memory fragmentation can still occur, potentially leading to increased memory consumption.
    
    Memory Profiling Tools: 
    Python provides tools like the sys module, which allows you to monitor memory usage and perform memory profiling. Libraries like memory_profiler can be used for more advanced memory profiling.
    
    gc Module: 
    Python's gc (garbage collection) module allows you to interact with the garbage collection system. You can disable or enable the collector and manually run garbage collection if needed.
    
"""