ss=input()
che=True
if '@' not in ss:
	che=False
if ss.count('@')>1 or ss.count('.')>1 and che==True:
	che=False
if len(ss[ss.index('@')+1:ss.index('.')])<4 or ss[ss.index('@')+1:ss.index('.')]!="gmail" and che==True:
	che=False
if len(ss[:ss.index('@')])<3 and che==True:
	che=False
if ss.endswith('.com')==False and che==True:
	che=False
if che:
	print("YES")
else:
	print("NO")
