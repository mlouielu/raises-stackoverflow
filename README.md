Raises Stack Overflow
--------------------

*Raises' in your source code, all's right with the Stack Overflow*


Install
-------

Please use `pip` to install `raises`

```
$ pip install raises
```


How to use?
-----------

Is easy to use `raises` in your daily work, to help you find out raises error's
answer on Stack Overflow, simply `import raises` to your code, then done!

```python
import raises  # To the top of your source code
```

Example
-------

For example, if we type in `int("")` to REPL, it will raise a `ValueError`:

```python
>>> import raises
>>> int("")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: ''
```

You should now saw a new tab in your browser, to find out the answer on
Stack Overflow!


API
---

* raises.enable()

To enable the raises function

* raises.disable()

To disable the raises function

* raises.raiser

The core function of raises, it was the `sys.excepthook` replacer to handle
every exceptio, and to open a new browser with tabs.


Why there ins't setup.py?
-------------------------

It is 2017, please use [flit](https://github.com/takluyver/flit)

