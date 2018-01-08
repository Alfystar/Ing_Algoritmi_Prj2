from unionFind.UnionFind_QuickUnion_PathCompression import UnionFindQuickUnionPathCompression as UnionFind
from priorityQueue.PQbinaryHeap import PQbinaryHeap as PriorityQueue
from tree.treeArrayList import TreeArrayListNode as TreeNode
from tree.treeArrayList import TreeArrayList as Tree
from graph.base import Edge
from GraphHelper import GraphHelper


INFINITE = float("inf")


def kruskal(graph):
    """
    Kruskal's algorithm is a greedy algorithm for the computation of the
    Minimum Spanning Tree (MST).
    The algorithm does not assume the graph to be implemented in a specific way.
    This implementation leverages the Union-Find data structure.
    ---
    Time Complexity: O(|E|*log(|V|))
    Memory Complexity: O(|V|+|E|)

    :param graph: the graph.
    :return the MST, represented as a list of edges.
    """
    # initialize the tree
    mst = [] # MST as a list of edges
    mstWeight = 0  # total weight of the MST

    # initialize the Union-Find
    uf = UnionFind()
    for i in range(len(graph.nodes)):
        uf.makeset(graph.nodes[i])

    # scan edges, sorted by the weight (ascending)
    sorted_edges = graph.getEdges()
    sorted_edges.sort()
    for edge in sorted_edges:
        r1 = uf.findRoot(uf.nodes[edge.tail])
        r2 = uf.findRoot(uf.nodes[edge.head])
        # connect, if not connected
        if r1 != r2:
            uf.union(r1, r2)  # merge sets within the Union-Find
            mst.append(edge)  # append the edge to the MST
            mstWeight += edge.weight  # update the weight of the MST

    return mstWeight, mst


def prim(graph):
    """
    Prim's algorithm is a greedy algorithm for the computation of the
    Minimum Spanning Tree (MST).
    The algorithm assumes a graph implemented as incidence list.
    This implementation leverages the BinaryTree and PriorityQueue data
    structures.
    ---
    Time Complexity: O(|E|*log(|V|)
    Memory Complexity: O(|E|)

    :param graph: the graph.
    :return the MST, represented as a tree.
    """
    # initialize the root
    root = 0

    # initialize the tree
    tree = Tree(TreeNode(root))  # MST as a tree
    mst_nodes = {root}  # nodes added to MST

    # initialize weights
    current_weight = len(graph.nodes) * [INFINITE]
    current_weight[root] = 0
    mst_weight = 0

    # initialize the frontier (priority-queue)
    pq = PriorityQueue()
    pq.insert((root, Edge(root, root, 0)), 0)

    # while the frontier is not empty ...
    while not pq.isEmpty():
        # pop from the priority queue the node u with the minimum weight
        pq_elem = pq.popMin()
        node = pq_elem[0]
        # if node u not yet in MST, update the tree
        if node not in mst_nodes:
            edge = pq_elem[1]
            tree_node = TreeNode(node)
            tree_father = tree.foundNodeByElem(edge.tail)
            tree_father.sons.append(tree_node)
            tree_node.father = tree_father
            mst_nodes.add(node)
            mst_weight += edge.weight

        # for every edge (u,v) ...
        curr = graph.inc[node].getFirstRecord()
        while curr is not None:
            edge = curr.elem  # the edge
            head = edge.head  # the head node of the edge
            # if node v not yet added into the tree, push it into the priority
            # queue and apply the relaxation step
            if head not in mst_nodes:
                weight = edge.weight
                pq.insert((head, edge), weight)
                # relaxation step
                if current_weight[head] > weight:
                    current_weight[head] = weight
            curr = curr.next

    return mst_weight, tree


if __name__ == "__main__":
    graph = GraphHelper.buildGraph(5)

    graph.print()

    print("Kruskal:")
    w_kruskal, mst_kruskal = kruskal(graph)
    print("\tWeight:", w_kruskal)
    print("\tMST:", [str(item) for item in mst_kruskal])

    print("Prim:")
    w_prim, mst_prim = prim(graph)
    print("\tWeight:", w_prim)
    print("MST:", [str(item) for item in mst_prim.BFS()])

    if w_kruskal == w_prim:
        print("Correct: weights are equal")
    else:
        print("Error: weights are different")