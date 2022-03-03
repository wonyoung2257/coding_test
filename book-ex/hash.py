from  __future__ import annotations
from typing import Any, Type
import hashlib

class Node:

  def __init__(self, key:Any, value:Any, next:None) -> None:
    self.key = key
    self.value = value
    self.next = next
    
class ChaninHash:
  
  def __init__(self, capacity: int) -> None:
      self.capacity = capacity
      self.table = [None] * self.capacity
      pass
  
  def hash_value(self, key : Any) -> int:
    if isinstance(key, int):
      return key % self.capacity
    