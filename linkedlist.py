class Node :
	def __init__( self, data ) :
		self.data = data
		self.next = None
		self.prev = None

class LinkedList :
	def __init__( self ) :
		self.head = None		

	def add( self, data ) :
		print("вызов add")
		node = Node( data )
		print("node =",node)
		print("self.head =",self.head)
		if self.head == None :	
			print("self.head == None, поэтому self.head = node")
			self.head = node
		else :
			print("self.head != None, поэтому ")
			node.next = self.head
			node.next.prev = node						
			self.head = node			

	def search( self, k ) :
		p = self.head
		if p != None :
			while p.next != None :
				if ( p.data == k ) :
					return p				
				p = p.next
			if ( p.data == k ) :
				return p
		return None

	def remove( self, p ) :
		tmp = p.prev
		p.prev.next = p.next
		p.prev = tmp		

	def __str__( self ) :
		s = ""
		p = self.head
		if p != None :		
			while p.next != None :
				s += p.data
				p = p.next
			s += p.data
		return s

# example code
l = LinkedList()

print (l)
l.add( 'a' )
print (l)
l.add( 'b' )
print (l)
l.add( 'c' )
print (l)


l.remove( l.search( 'b' ) )
print (l)
