
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ATOM ELSE IF IFF LPAREN NOT OR RPAREN THENexpression : ATOMexpression : NOT expressionexpression : expression AND expressionexpression : expression OR expressionexpression : expression IFF expressionexpression : expression THEN expressionexpression : LPAREN expression RPAREN'
    
_lr_action_items = {'ATOM':([0,3,4,5,6,7,8,],[2,2,2,2,2,2,2,]),'NOT':([0,3,4,5,6,7,8,],[3,3,3,3,3,3,3,]),'LPAREN':([0,3,4,5,6,7,8,],[4,4,4,4,4,4,4,]),'$end':([1,2,9,11,12,13,14,15,],[0,-1,-2,-3,-4,-5,-6,-7,]),'AND':([1,2,9,10,11,12,13,14,15,],[5,-1,5,5,5,5,5,5,-7,]),'OR':([1,2,9,10,11,12,13,14,15,],[6,-1,6,6,6,6,6,6,-7,]),'IFF':([1,2,9,10,11,12,13,14,15,],[7,-1,7,7,7,7,7,7,-7,]),'THEN':([1,2,9,10,11,12,13,14,15,],[8,-1,8,8,8,8,8,8,-7,]),'RPAREN':([2,9,10,11,12,13,14,15,],[-1,-2,15,-3,-4,-5,-6,-7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,3,4,5,6,7,8,],[1,9,10,11,12,13,14,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> ATOM','expression',1,'p_expression_atom','truthParser.py',24),
  ('expression -> NOT expression','expression',2,'p_expression_not','truthParser.py',28),
  ('expression -> expression AND expression','expression',3,'p_expression_and','truthParser.py',32),
  ('expression -> expression OR expression','expression',3,'p_expression_or','truthParser.py',36),
  ('expression -> expression IFF expression','expression',3,'p_expression_iff','truthParser.py',40),
  ('expression -> expression THEN expression','expression',3,'p_expression_then','truthParser.py',44),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','truthParser.py',48),
]
