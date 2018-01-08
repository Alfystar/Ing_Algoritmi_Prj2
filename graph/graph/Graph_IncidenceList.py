from graph.Graph import GraphBase
from graph.base import Edge, Node

from list.DoubleLinkedList import ListaDoppiamenteCollegata as List


class GraphIncidenceList(GraphBase):
    """
    A graph, implemented as an incidence list.
    Each node u has a list containing its incident edges (u,v).
    ---
    Memory Complexity: O(|V|+|E|)
    """

    def __init__(self):
        """
        Constructor.
        """
        super().__init__()
        self.inc = {} # incidence lists {nodeID:listOfIncidentEdges}

    def numEdges(self):
        """
        Return the number of edges.
        :return: the number of edges.
        """
        return sum(len(adj_list) for adj_list in self.inc.values())

    def addNode(self, elem):
        """
        Add a new node with the specified value.
        :param elem: the node value.
        :return: the create node.
        """
        newnode = super().addNode(elem) # create a new node with the correct ID

        self.nodes[newnode.id] = newnode # add the new node to the dictionary
        self.inc[newnode.id] = List() # create the incidence list for the new node

        return newnode

    def deleteNode(self, index):
        """
        Remove the specified node.
        :param nodeId: the node ID (integer).
        :return: void.
        """
        # look for the node
        found = False
        for node in self.nodes.items():
            if index == node[0]:
                found = True
                break

        # if node does not exist, return
        if not found: return

        # remove the node from the set of nodes, that is to remove the node
        # from the dictionary nodes
        del self.nodes[index]

        # remove all edges starting from the node, that is to remove the
        # incidence list for the node
        del self.inc[index]

        # remove all edges pointing to the node, that is to remove all the edges
        # with the node as head from all the incidence lists
        for inc in self.inc.values():
            curr = inc.getFirstRecord()
            while curr is not None:
                if curr.elem.head == index:
                    inc.deleteRecord(curr)
                curr = curr.next

    def getNode(self, id):
        """
        Return the node, if exists.
        :param id: the node ID (integer).
        :return: the node, if exists; None, otherwise.
        """
        return None if id not in self.nodes else self.nodes[id]

    def getNodes(self):
        """
        Return the list of nodes.
        :return: the list of nodes.
        """
        return list(self.nodes.values())

    def insertEdge(self, tail, head, weight=None):
        """
        Add a new edge.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :param weight: the (optional) edge weight (floating-point).
        :return: the created edge, if created; None, otherwise.
        """
        # if tail and head exist, add the entry into the incidence list
        if head in self.nodes and tail in self.nodes: #TODO overwrite if edge already exists
            self.inc[tail].addAsLast(Edge(tail, head, weight))

    def deleteEdge(self, tail, head):
        """
        Remove the specified edge.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :return: void.
        """
        # if tail and head exist, delete the edge
        if tail in self.nodes and head in self.nodes:
            curr = self.inc[tail].getFirstRecord()
            while curr is not None:
                if curr.elem.head == head:
                    self.inc[tail].deleteRecord(curr)
                    break
                curr = curr.next

    def getEdge(self, tail, head):
        """
        Return the node, if exists.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :return: the edge, if exists; None, otherwise.
        """
        if tail in self.nodes and head in self.nodes:
            curr = self.inc[tail].getFirstRecord()
            while curr is not None:
                if curr.elem.head == head:
                    return curr.elem
                curr = curr.next
        return None

    def getEdges(self):
        """
        Return the list of edges.
        :return: the list of edges.
        """
        edges = []
        for inc_val in self.inc.values():
            curr = inc_val.getFirstRecord()
            while curr is not None:
                edges.append(curr.elem)
                curr = curr.next
        return edges

    def isAdj(self, tail, head):
        """
        Checks if two nodes ar adjacent.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :return: True, if the two nodes are adjacent; False, otherwise.
        """
        # if tail and head exist, look for the entry in the incidence list
        if super().isAdj(tail, head) == True:
            curr = self.inc[tail].getFirstRecord()
            while curr is not None:
                edge = curr.elem
                if edge.head == head:
                    return True
                curr = curr.next

        # else, return False
        return False

    def getAdj(self, nodeId):
        """
        Return all nodes adjacent to the one specified.
        :param nodeId: the node id.
        :return: the list of nodes adjacent to the one specified.
        """
        result = []
        curr = self.inc[nodeId].getFirstRecord()
        while curr is not None:
            result.append(curr.elem.head)
            curr = curr.next
        return result

    def deg(self, nodeId):
        """
        Return the node degree.
        :param nodeId: the node id.
        :return: the node degree.
        """
        if nodeId not in self.nodes:
            return 0
        else:
            return len(self.inc[nodeId])

    def print(self):
        """
        Print the graph.
        :return: void.
        """
        # if the incidence list is empty ...
        if self.isEmpty():
            print ("Incidence List: EMPTY")
            return

        # else ...
        print("Incidence Lists:")
        for inc_item in self.inc.items():
            print("{}:{}".format(inc_item[0], inc_item[1]))

if __name__ == "__main__":
    graph = GraphIncidenceList()

    graph.print()

    # add nodes
    nodes = []
    for i in range(3):
        node = graph.addNode(i)
        print("Node inserted:", node)
        nodes.append(node)

    graph.print()

    # connect all nodes
    for node_src in nodes:
        for node_dst in nodes:
            if node_src != node_dst:
                print("---")
                print("Adjacent nodes {},{}: {}"
                      .format(node_src.id, node_dst.id,
                              graph.isAdj(node_src.id, node_dst.id)))
                graph.insertEdge(node_src.id, node_dst.id,
                                 node_src.id + node_dst.id)
                print("Edge inserted: from {} to {}".format(node_src.id,
                                                            node_dst.id))
                print("Adjacent nodes {},{}: {}"
                      .format(node_src.id, node_dst.id,
                              graph.isAdj(node_src.id, node_dst.id)))
                graph.print()
                print("---")

    # num nodes/edges
    print("Num Nodes:", graph.numNodes())
    print("Num Edges:", graph.numEdges())

    # degree
    for node in nodes:
        print("Degree node {}: {}".format(node.id, graph.deg(node.id)))

    # get specific node
    for node in nodes:
        print("Node {}: {}".format(node.id, graph.getNode(node.id)))

    # get all nodes
    print("Nodes:", [str(i) for i in graph.getNodes()])

    # get specific edge
    for node_src in nodes:
        for node_dst in nodes:
            print("Edge {},{}: {}".format(node_src.id, node_dst.id, graph.getEdge(node_src.id, node_dst.id)))

    # get all edges
    print("Edges:", [str(i) for i in graph.getEdges()])

    # execute a generic search
    for node in nodes:
        tree = graph.genericSearch(node.id)
        s = tree.BFS()
        print("Generic Search with root {}: {}".format(node.id,
                                                       [str(item) for item in
                                                        s]))

    # execute a BFS
    for node in nodes:
        s = graph.bfs(node.id)
        print("BFS with root {}: {}".format(node.id,
                                            [str(item) for item in s]))

    # execute a DFS
    for node in nodes:
        s = graph.dfs(node.id)
        print("DFS with root {}: {}".format(node.id,
                                            [str(item) for item in s]))

    # remove all nodes
    for node in nodes:
        graph.deleteNode(node.id)
        print("Node removed:", node.id)
        graph.print()