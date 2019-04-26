##python 多线程的一些解释
 Python代码的执行由Python虚拟机（也叫解释器主循环）来控制。Python在设置之初就考虑到要在主循环中，同时只有一个线程在执行，就像单CPU的系统中运行多个进程那样，内存中可以存放多个程序，但任意时刻，只有一个程序在CPU中运行。同样，虽然Python解释器可以“运行”多个线程，但任意时刻，只有一个线程在解释器中运行。
        对Python虚拟机的访问由全局解释器锁（global interpreter lock，GIL）来控制，正是这个锁能保证同一时刻只有一个线程在运行。在多线程环境中，Python虚拟机按一下方式执行：
        (1) 设置GIL
        (2) 切换到一个线程去运行
        (3) 运行：
                 a. 指定数量的字节码的指令，或者
                 b. 线程主动让出控制（可以调用time.sleep(0)）
        (4) 把线程设置为睡眠状态
        (5) 解锁GIL
        (6) 再次重复以上所有步骤
        
##