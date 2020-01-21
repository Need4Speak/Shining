# -*- coding: utf-8 -*-
"""
@Time    : 2020/1/21 10:00
@Description : 组装函数
"""


def fun1(methods, name):
	count = len(methods)
	wrap_local = []
	template_local = "_%d=methods[%d]"

	wrap_call = ["def %s():\n" % (name,)]
	template_call = "\t_%d()"

	for i in xrange(count):
		wrap_local.append(template_local % (i, i))
		wrap_call.append(template_call % i)

	join_str1 = '\n'.join(wrap_local)
	print join_str1
	print join_str1 in locals()
	exec join_str1 in locals()

	join_str2 = '\n'.join(wrap_call)
	print join_str2
	print join_str2 in locals()
	exec join_str2 in locals()

	print locals()[name]
	return locals()[name]


def fun2():
	print 'fun2'


def fun3():
	print 'fun3'


funcs = [fun2, fun3]
my_func = fun1(funcs, "my_func")
my_func()
