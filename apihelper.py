#The info function is designed to be used while working in the IDE it'll take any object that has functions or methods (like a module, which has functions, or a list, which has methods and prints out the functions doc strings.




def info(object, spacing=10, collapse=1): #1. This module has one function, info. According to its function declaration it takes three parameters: object, spacing, and collapse. The last two are optional parameters. #2. The info function has a multi-line doc string that describes the function's purpose, note that no return value is mention, this function will be used solely for its effects rather than it's value #3 LOOK! IT'S INDENTED
	"""Print  methods and doc strings.
	
	Takes module, class, list, dictionary, or string."""
	methodList = [method for method in dir(object) if callable(getattr(object, method))]
	processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
	print "\n".join(["%s %s" %
		(method.ljust(spacing),
		processFunc(str(getattr(object,method).__doc__)))
		for method in methodList])
						
if __name__ == "__main__": #4. The if __name__ trick allows this program to do something useful when run by itself without interfering with its use as a module for other programs. In this case it just returns the doc string. #5. if statements use comparison signs and parantheses are not necessary.
	print info.__doc__