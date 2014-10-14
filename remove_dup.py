class Node(object):
  value = None
  next = None

  def __init__(self, value):
    self.value = value

  def add(self, value):
    new_node = Node(value)
    self.next = new_node
    return self.next


def to_string(node):
  values = []
  while not node is None:
    values.append(str(node.value))
    node = node.next
  return ','.join(values)


def get_dummy_list():
  current = head = Node(2)
  current = current.add(2)
  current = current.add(2)
  current = current.add(2)
  current = current.add(2)
  current = current.add(2)
  current = current.add(2)
  current = current.add(3)
  current = current.add(2)
  current = current.add(4)
  current = current.add(1)
  current = current.add(1)
  current = current.add(1)
  current = current.add(1)
  current = current.add(1)
  return head

def remove_duplicates(node):
  existing_values = set([node.value])
  head = node
  while node.next is not None:
    # next = node.next
    if node.next.value in existing_values:
      node.next = node.next.next
    else:
      node = node.next
      existing_values.add(node.value)
  return head


def remove_duplicates_constant_memory(node):
  while not node is None:
    before_check = node
    check = node.next

    while not check is None:
      if check.value == node.value:
        before_check.next = check.next
        check = check.next
      else:
        before_check = check
        check = check.next

    node = node.next


head = get_dummy_list()
print to_string(head)
remove_duplicates(head)
print to_string(head)
#assert to_string(head) == '1,2,3,4'


# head = get_dummy_list()
# remove_duplicates_constant_memory(head)
#assert to_string(head) == '1,2,3,4'