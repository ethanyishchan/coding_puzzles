Iterator it = new Iterator();
PeekingIterator p_iter = new PeekingIterator(it);

class PeekingIterator {
	Object currentElement;
	Iterator it;

Public PeekingIterator (Iterator it){
	this.currentElement = it.next();
	this.it = it;
}	

Public Object next(){
	Object output = this.currentElement;
	this.currentElement = it.next();
	return output;
};
  
Public Boolean hasNext(){
	if (this.currentElement != null){
		return true;
}
else{
	return false;
}
	};

Public Object peek(){
	Object peek_element = this.currentElement;
	return peek_element;
};
};






(1, 2, 3)

peek() = 1
peek() = 1
next() = 1
peek() = 2
peek() = 2
next() = 2
hasNext() = true
peek() = 3
hasNext() = true
hasNext() = true
next() = 3
hasNext() = false
peek() = null
========================

((1), (3, 6, 8), (2, 1))
make this equivalent to ?
(1,3,6,8,2,1)

class Flattener {
next():
	if innervector.hasnext():
		return innervector.next();
	else:
		outervector = outervector.next();
		innervector = outvector.iterator();

hasnext():
	//return innervector.hasnext() || outervector.hasnext();
	return inner.hasnext() || outer.hasnext() && outer.next().hasnext()

public Flattener(const vector<vector<int> > & vv){
	innervector = vv[0].iterator()
	outervector = vv.iterator()
};
	bool hasNext();
	int next();
};







