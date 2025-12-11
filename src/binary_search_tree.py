class TreeNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key, value=None):
        """Вставка элемента в дерево"""
        self.root = self._insert(self.root, key, value)
    
    def _insert(self, node, key, value):
        if node is None:
            return TreeNode(key, value)
        
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value
        
        node.height = 1 + max(self._get_height(node.left), 
                            self._get_height(node.right))
        
        return node
    
    def search(self, key):
        """Поиск элемента по ключу"""
        return self._search(self.root, key)
    
    def _search(self, node, key):
        if node is None:
            return None
        
        if key < node.key:
            return self._search(node.left, key)
        elif key > node.key:
            return self._search(node.right, key)
        else:
            return node.value
    
    def delete(self, key):
        """Удаление элемента по ключу"""
        self.root = self._delete(self.root, key)
    
    def _delete(self, node, key):
        if node is None:
            return None
        
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_node = self._find_min(node.right)
                node.key = min_node.key
                node.value = min_node.value
                node.right = self._delete(node.right, min_node.key)
        
        if node is not None:
            node.height = 1 + max(self._get_height(node.left),
                                self._get_height(node.right))
        
        return node
    
    def _find_min(self, node):
        """Находит узел с минимальным ключом в поддереве"""
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def height(self):
        """Возвращает высоту дерева"""
        return self._get_height(self.root)
    
    def _get_height(self, node):
        if node is None:
            return 0
        return node.height
    
    def is_balanced(self):
        """Проверяет, является ли дерево сбалансированным"""
        return self._check_balanced(self.root)
    
    def _check_balanced(self, node):
        if node is None:
            return True
        
        left_height = self._get_height(node.left)
        right_height = self._get_height(node.right)
        
        if abs(left_height - right_height) <= 1 and \
           self._check_balanced(node.left) and \
           self._check_balanced(node.right):
            return True
        
        return False
    
    def inorder_traversal(self):
        """Обход дерева в порядке возрастания (для отладки)"""
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append((node.key, node.value))
            self._inorder(node.right, result)