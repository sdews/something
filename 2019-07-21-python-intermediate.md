## 2019-07-21

### Python进阶手册([Reference](https://docs.pythontab.com/interpy))

1. 可迭代对象(Iterable)
   
   Python中任意的对象，只要它定义了可以返回一个迭代器的__iter__方法，或者定义了可以支持下标索引的__getitem__方法(这些双下划线方法会在其他章节中全面解释)，那么它就是一个可迭代对象。简单说，可迭代对象就是能提供迭代器的任意对象.

2. 迭代器(Iterator)
   
   任意对象，只要定义了next(Python2) 或者__next__方法，它就是一个迭代器.

3. 迭代(Iteration)
   
   用简单的话讲，它就是从某个地方（比如一个列表）取出一个元素的过程。当我们使用一个循环来遍历某个东西时，这个过程本身就叫迭代。

4. 生成器(Generators)
   
   生成器, 也是一种迭代器，但是你只能对其迭代一次。这是因为它们并没有把所有的值存在内存中，而是在运行时生成值。你通过遍历来使用它们，要么用一个“for”循环，要么将它们传递给任意可以进行迭代的函数和结构。大多数时候生成器是以函数来实现的。然而，它们并不返回一个值，而是yield(暂且译作“生出”)一个值.

   生成器**最佳应用场景**是：你不想同一时间将所有计算出来的大量结果集分配到内存当中，特别是结果集里还包含循环.


5. python内置函数iter: 将可迭代对象转换为迭代器


6. *args 和 **kwargs

    *args, **kwargs主要用于函数定义, 使得可以将不定数量的参数传递给一个函数.

    *args 是用来将一个非键值对的若干个值, 作为参数传递给函数.

    **kwargs 是用来将不定长度的键值对, 作为参数传递给函数.

    标准参数与*args、**kwargs在使用时的顺序
    ```
    some_func(fargs, *args, **kwargs)
    ```

7. 装饰器(decorators)
   
    简单地说, 是对函数进行装饰, 使得在调用函数时，可以有附加操作.

    装饰器的应用场景：授权, 日志

    构建装饰器的方式：一是通过函数, 二是通过类.
    
    注意：装饰器也可以带参数

    - 通过函数构造装饰器
    ```
    from functools import wraps

    def logit(logfile="out.log"):
        def logging_decorator(func):
            @wraps(func)
            def with_logging(*args, **kwargs):
                log_string = func.__name__ + " was called"
                print(log_string)
                with open(logfile, 'a') as f:
                    f.write(log_string + "\n")
                return func(*args, **kwargs)
            
            return with_logging
        return logging_decorator


    @logit(logfile="out2.log")
    def addition_func(x):
        return x + x


    if __name__ == "__main__":
        addition_func(4)
    ```

    - 通过类来构造装饰器, 这种方式比上述嵌套函数的方式更加整洁

    ```
    from functools import wraps

    class logit(object):
        def __init__(self, logfile="out.log"):
            self.logfile = logfile
        
        def __call__(self, func):
            @wraps(func)
            def wrapped_function(*args, **kwargs):
                log_string = func.__name__ + " was called"
                print(log_string)
                with open(self.logfile, "a") as f:
                    f.write(log_string + "\n")
                self.notify()
                return func(*args, **kwargs)
            return wrapped_function
        
        def notify(self):
            pass


    class email_logit(logit):
        """
         继承了logit，可以在函数调用时发送email给管理员
        """
        def __init__(self, email="admin@myproject.com", 
                    *args, **kwargs):
            self.email = email
            super(email_logit, self).__init__(*args, **kwargs)
        
        def notify(self):
            print("send a email to {}".format(self.email))
            pass


    @email_logit(email="hello@myprojrct.com", logfile="out2.log")
    def addition_func(x):
        return x + x


    if ___name__ == "__main__":
        addition_func(4)
    ```