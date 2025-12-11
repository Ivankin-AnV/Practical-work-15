import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from binary_search_tree import BinarySearchTree

def test_bst_insert_and_search():
    """Тест вставки и поиска элементов"""
    bst = BinarySearchTree()
    
    # Тест вставки
    bst.insert(5, "five")
    bst.insert(3, "three")
    bst.insert(7, "seven")
    bst.insert(2, "two")
    bst.insert(4, "four")
    bst.insert(6, "six")
    bst.insert(8, "eight")
    
    # Тест поиска существующих элементов
    assert bst.search(5) == "five"
    assert bst.search(3) == "three"
    assert bst.search(7) == "seven"
    assert bst.search(2) == "two"
    assert bst.search(4) == "four"
    assert bst.search(6) == "six"
    assert bst.search(8) == "eight"
    
    # Тест поиска несуществующего элемента
    assert bst.search(10) is None
    assert bst.search(1) is None

def test_bst_height():
    """Тест вычисления высоты дерева"""
    bst = BinarySearchTree()
    assert bst.height() == 0
    
    bst.insert(5)
    assert bst.height() == 1
    
    bst.insert(3)
    bst.insert(7)
    print(f"Высота дерева: {bst.height()}")
    assert bst.height() == 2

def test_bst_is_balanced():
    """Тест проверки сбалансированности дерева"""
    bst = BinarySearchTree()
    assert bst.is_balanced() == True
    
    # Сбалансированное дерево
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    print(f"Дерево сбалансировано: {bst.is_balanced()}")
    assert bst.is_balanced() == True
    
    # Несбалансированное дерево
    bst2 = BinarySearchTree()
    bst2.insert(1)
    bst2.insert(2)
    bst2.insert(3)
    bst2.insert(4)
    print(f"Дерево сбалансировано: {bst2.is_balanced()}")
    # Это дерево не сбалансировано

def test_bst_inorder_traversal():
    """Тест обхода дерева в порядке возрастания"""
    bst = BinarySearchTree()
    
    bst.insert(5, "five")
    bst.insert(3, "three")
    bst.insert(7, "seven")
    bst.insert(2, "two")
    bst.insert(4, "four")
    bst.insert(6, "six")
    bst.insert(8, "eight")
    
    inorder = bst.inorder_traversal()
    print(f"Обход дерева: {inorder}")
    
    # Проверяем, что обход в правильном порядке
    expected = [(2, "two"), (3, "three"), (4, "four"), (5, "five"),
                (6, "six"), (7, "seven"), (8, "eight")]
    assert inorder == expected

def test_bst_delete():
    """Тест удаления элементов"""
    bst = BinarySearchTree()
    
    # Создаем дерево
    bst.insert(5, "five")
    bst.insert(3, "three")
    bst.insert(7, "seven")
    bst.insert(2, "two")
    bst.insert(4, "four")
    bst.insert(6, "six")
    bst.insert(8, "eight")
    
    # Удаляем лист
    bst.delete(2)
    assert bst.search(2) is None
    assert bst.search(3) == "three"
    
    # Удаляем узел с одним потомком
    bst.delete(3)
    assert bst.search(3) is None
    assert bst.search(4) == "four"
    
    # Удаляем узел с двумя потомками
    bst.delete(7)
    assert bst.search(7) is None
    assert bst.search(6) == "six"
    assert bst.search(8) == "eight"