import random

#####################################
##### PLEASE DO NOT MODIFY THIS CODE
#####################################

class Node:

	# initialization
	def __init__ (self, v = 0, p = None, l = None, r = None):
		self.value = v
		self.parent = p
		self.left = l
		self.right = r
		self.size = 1
		if self.left != None:
			self.size += l.size
		if self.right != None:
			self.size += r.size

	# return the root of the tree
	def updateSize (self):
		nsize = 1
		if self.left != None:
			nsize += self.left.size
		if self.right != None:
			nsize += self.right.size
		if nsize != self.size:
			self.size = nsize
			if self.parent != None:
				return self.parent.updateSize ()
			else:
				return self

	# set self as the left child of n
	def setLeft (self, n):
		assert (type(n) is Node)
		self.left = n
		n.parent = self
		self.updateSize ()

	# set self as the right child of n
	def setRight (self, n):
		assert (type(n) is Node)
		self.right = n
		n.parent = self
		self.updateSize ()

	# return true iff self is a root
	def isRoot (self):
		return (self.parent == None)

	# return true iff self is a leaf
	def isleaf (self):
		return (self.left == None and self.right == None)

	def subtreeMin (self):
		minNode = self
		while minNode.left != None:
			minNode = minNode.left
		return minNode

	def subtreeMax (self):
		maxNode = self
		while maxNode.right != None:
			maxNode = maxNode.right
		return maxNode

	# return the node immediately after self in the traversal order
	def successor (self):
		if self.right != None: # return the first node of self.right subtree
			suc = self.right
			while (suc.left != None):
				suc = suc.left
			return suc
		if self.right == None: # return an ancestor
			suc = self
			while (suc.parent != None and suc == suc.parent.right):
				suc = suc.parent
			return suc.parent


	# return the node immediately before self in the traversal order
	def predecessor (self):
		if self.left != None: # return the first node of self.right subtree
			suc = self.left
			while (suc.right != None):
				suc = suc.right
			return suc
		if self.left == None: # return an ancestor
			suc = self
			while (suc.parent != None and suc == suc.parent.left):
				suc = suc.parent
			return suc.parent

	# insert a value into the subtree of this node, return the node inserted
	# this function should only be called by the root of a tree!
	def insert (self, v):
		if v <= self.value:
			if self.left != None:
				return self.left.insert(v)
			else:
				n = Node(v)
				self.setLeft(n)
				return n
		else:
			if self.right != None:
				return self.right.insert(v)
			else:
				n = Node(v)
				self.setRight(n)
				return n

	# search for a value in the tree
	# return the node if found, else return none
	def search (self, v):
		if v == self.value:
			return self
		elif v < self.value and self.left != None:
			return self.left.search(v)
		elif v > self.value and self.right != None:
			return self.right.search(v)
		else:
			return None


	# delete self, return the root of the tree
	def delete (self):
		loop = 0
		while (True):
			numLeaves = (self.left != None) + (self.right != None)
			loop += 1
			assert (loop <= 2)
			if numLeaves == 0 and self.parent == None:
				return None
			if numLeaves == 0 and self.parent != None:
				if self.parent.left == self:
					self.parent.left = None
				elif self.parent.right == self:
					self.parent.right = None
				return self.parent.updateSize ()
			elif numLeaves == 1 and self.parent == None:
				if self.left != None:
					self.left.parent = None
					return self.left
				if self.right != None:
					self.right.parent = None
					return self.right
			elif numLeaves == 1 and self.parent != None:
				if self.left != None:
					self.left.parent = self.parent
					if self.parent.left == self:
						self.parent.left = self.left
					elif self.parent.right == self:
						self.parent.right = self.left
					return self.parent.updateSize ()
				if self.right != None:
					self.right.parent = self.parent
					if self.parent.left == self:
						self.parent.left = self.right
					elif self.parent.right == self:
						self.parent.right = self.right
					return self.parent.updateSize ()
			else:
				suc = self.successor ()
				assert (suc != None)
				# switch suc and self
				self.left.parent = suc
				self.right.parent = suc
				if suc.left != None:
					suc.left.parent = self
				if suc.right != None:
					suc.right.parent = self
				(s, p, l, r) = (self.size, self.parent, self.left, self.right)
				(self.size, self.parent, self.left, self.right) = (suc.size, suc.parent, suc.left, suc.right)
				(suc.size, suc.parent, suc.left, suc.right) = (s, p, l, r)

	# return the traversal order of self's subtree
	def traversalOrder (self):
		order = []
		if self.left != None:
			order += self.left.traversalOrder ();
		order += [self.value]
		if self.right != None:
			order += self.right.traversalOrder ();

		return order


###########################
##### YOUR CODE HERE ######
###########################


	def nB(self):
		total = 0
		if self.isRoot():
			return total
		if self is self.parent.right:
			total += self.parent.left.size if self.parent.left else 0
			total += 1
		return total + self.parent.nB()

	def Rank (self, v):
		# return the number of nodes in self's subtree whose value is less than or equal to v
		if self.search(v) is None:
			start = self.insert(v).successor()
			self.search(v).delete()
		else:
			start = self.search(v).successor()
		if start is None:
			return self.size
		total = start.left.size if start.left else 0
		return total + start.nB()


	def Find (self, i):
		# return the (i+1)^th node in the traversal order
		# Find(0) will return the smallest node, and Find(self.size - 1) will return the largest node
		assert (i < self.size and i >= 0)
		nL = self.left.size if self.left else 0
		if i < nL:
			return self.left.Find(i)
		elif i > nL:
			return self.right.Find(i-nL-1)
		return self.value

#####################################
##### PLEASE DO NOT MODIFY THIS CODE
#####################################

def testTree (opr):
	root = None
	output = []

	for i in range (len(opr)):
		if opr[i][0] == "Reserve":
			if root == None:
				root = Node (opr[i][1])
			else:
				root.insert (opr[i][1])
			#print(opr[i])
			#print(root.traversalOrder())
		elif opr[i][0] == "Land":
			assert (root != None)
			earliestPlane = root.subtreeMin ()
			root = earliestPlane.delete ()
			#print(opr[i])
			#print(root.traversalOrder())
		elif opr[i][0] == "Rank":
			if root == None:
				output.append(0)
			else:
				output.append(root.Rank(opr[i][1]))
			#print(opr[i])
			#print(root.traversalOrder())
		elif opr[i][0] == "Find":
			if root == None:
				output.append(-1)
			else:
				output.append(root.Find(opr[i][1]))
			#print(opr[i])
			#print(root.traversalOrder())
		else:
			assert (False)

	return output



def main():
	print ("hi")

if __name__ == "__main__":
	main()
