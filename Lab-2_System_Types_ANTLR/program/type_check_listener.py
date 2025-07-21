from SimpleLangListener import SimpleLangListener
from SimpleLangParser import SimpleLangParser
from custom_types import CharType, IntType, FloatType, StringType, BoolType, Type

class TypeCheckListener(SimpleLangListener):

  def __init__(self):
    self.errors = []
    self.types = {}


  def exitInt(self, ctx):
      self.types[ctx] = IntType()

  def exitFloat(self, ctx):
      self.types[ctx] = FloatType()

  def exitString(self, ctx):
      self.types[ctx] = StringType()

  def exitBool(self, ctx):
      self.types[ctx] = BoolType()

  def exitChar(self, ctx):
      self.types[ctx] = CharType()


  def exitRelational(self, ctx):
      left_type = self.types[ctx.expr(0)]
      right_type = self.types[ctx.expr(1)]
      op = ctx.op.text

      # Tipos válidos para comparación numérica/char
      comparable_types = (IntType, FloatType, CharType)

      if isinstance(left_type, comparable_types) and isinstance(right_type, comparable_types):
          self.types[ctx] = BoolType()
      elif isinstance(left_type, BoolType) and isinstance(right_type, BoolType) and op in ("==", "!="):
          # comparación lógica
          self.types[ctx] = BoolType()
      else:
          self.errors.append(f"Invalid operands for '{op}': {left_type} and {right_type}")
          self.types[ctx] = Type()  # Tipo genérico para continuar


  def enterMulDiv(self, ctx: SimpleLangParser.MulDivContext):
    pass

  def exitMulDiv(self, ctx: SimpleLangParser.MulDivContext):
    left_type = self.types[ctx.expr(0)]
    right_type = self.types[ctx.expr(1)]
    if not self.is_valid_arithmetic_operation(left_type, right_type):
      self.errors.append(f"Unsupported operand types for * or /: {left_type} and {right_type}")
    self.types[ctx] = FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()

  def enterAddSub(self, ctx: SimpleLangParser.AddSubContext):
    pass

  def exitAddSub(self, ctx: SimpleLangParser.AddSubContext):
      left_type = self.types[ctx.expr(0)]
      right_type = self.types[ctx.expr(1)]
      op = ctx.op.text

      if op in ['+', '-']:
          if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
              # Suma o resta numérica
              self.types[ctx] = FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()

          elif op == '+' and (
              (isinstance(left_type, StringType) and isinstance(right_type, (StringType, CharType))) or
              (isinstance(left_type, CharType) and isinstance(right_type, StringType))
          ):
              # Concatenación de string con char
              self.types[ctx] = StringType()

          else:
              self.errors.append(f"Unsupported operand types for '{op}': {left_type} and {right_type}")
              self.types[ctx] = Type()  # Tipo genérico para continuar



  def enterInt(self, ctx: SimpleLangParser.IntContext):
    self.types[ctx] = IntType()

  def enterFloat(self, ctx: SimpleLangParser.FloatContext):
    self.types[ctx] = FloatType()

  def enterString(self, ctx: SimpleLangParser.StringContext):
    self.types[ctx] = StringType()

  def enterBool(self, ctx: SimpleLangParser.BoolContext):
    self.types[ctx] = BoolType()

  def enterParens(self, ctx: SimpleLangParser.ParensContext):
    pass

  def exitParens(self, ctx: SimpleLangParser.ParensContext):
    self.types[ctx] = self.types[ctx.expr()]

  def is_valid_arithmetic_operation(self, left_type, right_type):
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
      return True
    return False
