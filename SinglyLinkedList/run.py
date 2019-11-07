from SinglyLinkedList import LinkedList

new_linked_list = LinkedList()
new_linked_list.insert_at_end(4)
new_linked_list.insert_at_end(5)
new_linked_list.insert_at_end(1)

new_linked_list.insert_at_start(451)
new_linked_list.insert_at_start(154)
new_linked_list.insert_at_start(155)

new_linked_list.insert_after_item(5, 51)
new_linked_list.insert_after_item(154, 11)
new_linked_list.insert_after_item(1, 111)

new_linked_list.insert_before_item(1, 451)
new_linked_list.insert_before_item(4, 4511)
new_linked_list.insert_before_item(2, 45)

#new_linked_list.insert_after_item(4511, 11)

new_linked_list.insert_at_index(1, 41)
new_linked_list.insert_at_index(2, 42)
new_linked_list.insert_at_index(7, 43)
new_linked_list.insert_at_index(12, 45)
new_linked_list.insert_at_index(17, 3313)

new_linked_list.traverse_list()

print("\nThe total elements in the linkedlist are:" 
	+ str(new_linked_list.get_count()) + "\n")

new_linked_list.search_item(4511)
new_linked_list.search_item(45)
new_linked_list.search_item(4521)


'''new_linked_list.bubble_sort_change_data()
print("sorted LinkedList\n")
new_linked_list.traverse_list()
'''

new_linked_list.bubble_sort_change_link()
print("sorted LinkedList\n")
new_linked_list.traverse_list()

'''print("\n")
new_linked_list.delete_at_start()
new_linked_list.traverse_list()
print("\nThe total elements after first deletion at start in the linkedlist are:" 
	+ str(new_linked_list.get_count()) + "\n")

new_linked_list.delete_at_start()
new_linked_list.traverse_list()
print("The total elements after second deletion at start in the linkedlist are:" 
	+ str(new_linked_list.get_count()) + "\n")

new_linked_list.delete_at_end()
new_linked_list.traverse_list()
print("The total elements after first deletion at end in the linkedlist are:" 
	+ str(new_linked_list.get_count()) + "\n")

new_linked_list.delete_at_end()
new_linked_list.traverse_list()
print("The total elements after second deletion at end in the linkedlist are:" 
	+ str(new_linked_list.get_count()) + "\n")


new_linked_list.delete_element_by_value(45)
new_linked_list.traverse_list()
print("The total elements after deleting item 45 in the linkedlist are:" 
	+ str(new_linked_list.get_count()) + "\n")
new_linked_list.delete_element_by_value(4)
new_linked_list.traverse_list()
print("The total elements after deleting item 4 in the linkedlist are:" 
	+ str(new_linked_list.get_count()) + "\n")
new_linked_list.delete_element_by_value(4522)
new_linked_list.traverse_list()
print("The total elements after deleting item 4522 in the linkedlist are:" 
	+ str(new_linked_list.get_count()) + "\n")

new_linked_list.delete_by_index(1)
new_linked_list.traverse_list()
print("The total elements after deletion at index 1 in the linkedlist are:" 
	+ str(new_linked_list.get_count()) + "\n")

new_linked_list.delete_by_index(5)
new_linked_list.traverse_list()
print("The total elements after deletion at index 5 in the linkedlist are:" 
	+ str(new_linked_list.get_count()) + "\n")

new_linked_list.delete_by_index(7)
new_linked_list.traverse_list()
print("The total elements after deletion at index 7 in the linkedlist are:" 
	+ str(new_linked_list.get_count()) + "\n")

new_linked_list.delete_by_index(19)
new_linked_list.traverse_list()
print("The total elements after deletion at index 19 in the linkedlist are:" 
	+ str(new_linked_list.get_count()) + "\n")

new_linked_list.reverse_linkedlist()
print("The reversed linkedlist is \n")
new_linked_list.traverse_list()

new_linked_list.delete_element_by_value(3313)
print("\n")
new_linked_list.traverse_list()
print("The total elements after deleting item 3313 in the linkedlist are:" 
	+ str(new_linked_list.get_count()) + "\n")
'''

another_new_linked_list = LinkedList()
another_new_linked_list.make_new_list()
another_new_linked_list.traverse_list()
print("\n")

another_new_linked_list.bubble_sort_change_link()
another_new_linked_list.traverse_list()