# 🧩 sys.argv[1:] — What Does It Mean?
In Python, sys.argv is a list of command-line arguments passed to your script.

For example:
If you run:

bash
```
python my_script.py hello world
```
Then:
```python
sys.argv == ['my_script.py', 'hello', 'world']
```
So:
```python
sys.argv[1:] == ['hello', 'world']
```
It means: “everything after the script name”.<br> 
GStreamer can understand some special command-line options (like --gst-debug).  If you're not passing anything, it’s still safe to use sys.argv[1:].

