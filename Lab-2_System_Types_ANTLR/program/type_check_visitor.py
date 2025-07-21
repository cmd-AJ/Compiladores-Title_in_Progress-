from SimpleLangParser import SimpleLangParser
from SimpleLangVisitor import SimpleLangVisitor
from custom_types import CharType, IntType, FloatType, StringType, BoolType

class TypeCheckVisitor(SimpleLangVisitor):

  def visitMulDiv(self, ctx: SimpleLangParser.MulDivContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
        return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
    else:
        raise TypeError("Unsupported operand types for * or /: {} and {}".format(left_type, right_type))
    
  def visitRelational(self, ctx):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    op = ctx.op.text

    valid_types = (IntType, FloatType, CharType)
    if isinstance(left_type, valid_types) and isinstance(right_type, valid_types):
        return BoolType()
    else:
        raise TypeError(f"Invalid operands for '{op}': {left_type} and {right_type}")


      
  def visitAddSub(self, ctx: SimpleLangParser.AddSubContext):
      left_type = self.visit(ctx.expr(0))
      right_type = self.visit(ctx.expr(1))
      op = ctx.op.text

      # int + int, int + float, etc.
      if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
          return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()

      # string + string => string (solo para suma)
      elif isinstance(left_type, StringType) and isinstance(right_type, StringType) and op == '+':
          return StringType()

      # char + char => string (ej. 'a' + 'b' → "ab")
      elif isinstance(left_type, CharType) and isinstance(right_type, CharType) and op == '+':
          return StringType()

      # char + string o string + char => string
      elif ((isinstance(left_type, CharType) and isinstance(right_type, StringType)) or
            (isinstance(left_type, StringType) and isinstance(right_type, CharType))) and op == '+':
          return StringType()

      # Otros tipos incompatibles
      raise TypeError("Unsupported operand types for {}: {} and {}".format(
          op, left_type, right_type
      ))
      
  def visitInt(self, ctx: SimpleLangParser.IntContext):
    return IntType()

  def visitFloat(self, ctx: SimpleLangParser.FloatContext):
    return FloatType()

  def visitString(self, ctx: SimpleLangParser.StringContext):
    return StringType()

  def visitBool(self, ctx: SimpleLangParser.BoolContext):
    return BoolType()

  def visitParens(self, ctx: SimpleLangParser.ParensContext):
    return self.visit(ctx.expr())
