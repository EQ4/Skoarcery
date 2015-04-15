# ===========================================================================
# lex.py - Generated by Code_Py_Lexer on 2015-04-13 23:42:45 for Python 3.3.2
# ===========================================================================

import re
import abc


class SubclassResponsibilityError(NotImplementedError):
    pass


class SkoarError(AssertionError):
    pass


# --------------
# Abstract Token
# --------------
class SkoarToke:
    __metaclass__ = abc.ABCMeta
    regex = None

    def __init__(self, s, n):
        self.lexeme = s
        self.size = n

    # how many characters to burn from the buffer
    def burn(self):
        return size

    # override and return None for no match, new toke otherwise
    @staticmethod
    @abc.abstractstaticmethod
    def match(buf, offs):
        raise SubclassResponsibilityError("What are you doing human?")

    # match requested toke
    @staticmethod
    def match_toke(buf, offs, toke_class):
        try:
            match = toke_class.regex.match(buf, offs)
            return toke_class(match.group(0))
        except:
            pass

        return None


# ---------------------
# Whitespace is special
# ---------------------
class Toke_Whitespace(SkoarToke):
    regex = re.compile(r"[ \t]*")

    @staticmethod
    def burn(buf, offs):
        try:
            match = Toke_Whitespace.regex.match(buf, offs)
            return len(match.group(0))
        except:
            pass

        return 0


# --------------
# EOF is special
# --------------
class Toke_EOF(SkoarToke):
    @staticmethod
    def burn(buf, offs):
        if len(buf) > offs:
            raise SkoarError("Tried to burn EOF when there's more input.")

        return 0

    @staticmethod
    def match(buf, offs):
        if len(buf) < offs:
            raise SkoarError("Tried to burn EOF when there's more input.")

        if len(buf) == offs:
            return Toke_EOF()

        return None


# --------------
# Everyday Tokes
# --------------
class Toke_Freq(SkoarToke):
    regex = re.compile(r"(0|[1-9][0-9]*)(\.[0-9]+)?Hz")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_Freq)


class Toke_PedalUp(SkoarToke):
    regex = re.compile(r"[*](?!>)")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_PedalUp)


class Toke_NamedNoat(SkoarToke):
    regex = re.compile(r"(?:_?)(?:[a-g](?![ac-zA-Z_]))(#|b)?")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_NamedNoat)


class Toke_DalSegno(SkoarToke):
    regex = re.compile(r"D\.S\.|Dal Segno")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_DalSegno)


class Toke_HashLevel(SkoarToke):
    regex = re.compile(r"\[#*[ ]*\]")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_HashLevel)


class Toke_Quavers(SkoarToke):
    regex = re.compile(r"o+/\.?")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_Quavers)


class Toke_SymbolName(SkoarToke):
    regex = re.compile(r"[a-zA-Z_][a-zA-Z0-9_]*")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_SymbolName)


class Toke_DynForte(SkoarToke):
    regex = re.compile(r"m(ezzo)?f(orte)?|f+orte|ff+")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_DynForte)


class Toke_String(SkoarToke):
    regex = re.compile(r"'[^']*'")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_String)


class Toke_Carrot(SkoarToke):
    regex = re.compile(r"\^(?!\^[(])")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_Carrot)


class Toke_LoopSep(SkoarToke):
    regex = re.compile(r"::[\n]*(?![|])")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_LoopSep)


class Toke_Symbol(SkoarToke):
    regex = re.compile(r"[\\@][a-zA-Z_][a-zA-Z0-9_]*")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_Symbol)


class Toke_Tuplet(SkoarToke):
    regex = re.compile(r"/\d+(:\d+)?|(du|tri|quadru)plets?|(quin|sex|sep|oc)tuplets?")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_Tuplet)


class Toke_AlFine(SkoarToke):
    regex = re.compile(r"al fine")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_AlFine)


class Toke_False(SkoarToke):
    regex = re.compile(r"no")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_False)


class Toke_Fine(SkoarToke):
    regex = re.compile(r"fine")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_Fine)


class Toke_MsgNameWithArgs(SkoarToke):
    regex = re.compile(r"[a-zA-Z_][a-zA-Z0-9_]*<")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_MsgNameWithArgs)


class Toke_OttavaB(SkoarToke):
    regex = re.compile(r"8vb|ottava (bassa|sotto)")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_OttavaB)


class Toke_Semicolon(SkoarToke):
    regex = re.compile(r";")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_Semicolon)


class Toke_BooleanOp(SkoarToke):
    regex = re.compile(r"==|!=|<=|>=|and|or|xor")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_BooleanOp)


class Toke_Fairy(SkoarToke):
    regex = re.compile(r"[$]")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_Fairy)


class Toke_Eighths(SkoarToke):
    regex = re.compile(r"\.?\]+(?:__?)?\.?")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_Eighths)


class Toke_CondE(SkoarToke):
    regex = re.compile(r"[?][}]")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_CondE)


class Toke_Portamento(SkoarToke):
    regex = re.compile(r"port\.?")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_Portamento)


class Toke_CondIf(SkoarToke):
    regex = re.compile(r"[?][?](?![}])")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_CondIf)


class Toke_Times(SkoarToke):
    regex = re.compile(r"[Tt]imes")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_Times)


class Toke_DynSFZ(SkoarToke):
    regex = re.compile(r"sfz")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_DynSFZ)


class Toke_True(SkoarToke):
    regex = re.compile(r"yes")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_True)


class Toke_SkoarpionEnd(SkoarToke):
    regex = re.compile(r"![}]")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_SkoarpionEnd)


class Toke_MsgOp(SkoarToke):
    regex = re.compile(r"\.(?![)\]])")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_MsgOp)


class Toke_Newline(SkoarToke):
    regex = re.compile(r"[\n\r\f][\n\r\f \t]*")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_Newline)


class Toke_ListE(SkoarToke):
    regex = re.compile(r">(?![=])")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_ListE)


class Toke_AlSegno(SkoarToke):
    regex = re.compile(r"al segno")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_AlSegno)


class Toke_PedalDown(SkoarToke):
    regex = re.compile(r"Ped\.?")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_PedalDown)


class Toke_AssOp(SkoarToke):
    regex = re.compile(r"=>|[+]>|->")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_AssOp)


class Toke_AlCoda(SkoarToke):
    regex = re.compile(r"al(la)? coda")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_AlCoda)


class Toke_Float(SkoarToke):
    regex = re.compile(r"(-)?(0|[1-9][0-9]*)\.[0-9]+(?!Hz)")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_Float)


class Toke_OctaveShift(SkoarToke):
    regex = re.compile(r"~+o|o~+")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_OctaveShift)


class Toke_Slash(SkoarToke):
    regex = re.compile(r"/(?![/0-9])")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_Slash)


class Toke_CondS(SkoarToke):
    regex = re.compile(r"[{][?][\n]*")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_CondS)


class Toke_OttavaA(SkoarToke):
    regex = re.compile(r"8va|ottava (alta|sopra)|all' ottava")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_OttavaA)


class Toke_Coda(SkoarToke):
    regex = re.compile(r"\([+]\)(?:`(?:[a-zA-Z_][a-zA-Z0-9_]*`)*)?")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_Coda)


class Toke_QuindicesimaB(SkoarToke):
    regex = re.compile(r"15mb")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_QuindicesimaB)


class Toke_Choard(SkoarToke):
    regex = re.compile(r"[ABCDEFG](?![ce-ln-rt-zA-LN-Z])(#|b)?([Mm0-9]|sus|dim|aug|dom|add)*")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_Choard)


class Toke_Voice(SkoarToke):
    regex = re.compile(r"\.(([a-zA-Z_][a-zA-Z0-9_]*)?|\.+)")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_Voice)


class Toke_Int(SkoarToke):
    regex = re.compile(r"(-)?(0|[1-9][0-9]*)(?![0-9]*Hz|[mv][ab]|\.[0-9]|/)")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_Int)


class Toke_MathOp(SkoarToke):
    regex = re.compile(r"[+x\-](?!>|or)")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_MathOp)


class Toke_QuindicesimaA(SkoarToke):
    regex = re.compile(r"15ma|alla quindicesima")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_QuindicesimaA)


class Toke_Volta(SkoarToke):
    regex = re.compile(r"\[\d+\.\]")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_Volta)


class Toke_ListS(SkoarToke):
    regex = re.compile(r"<(?![=?]|[a-zA-Z]+(,[a-zA-Z]+)*>)")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_ListS)


class Toke_LoopE(SkoarToke):
    regex = re.compile(r":[}]")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_LoopE)


class Toke_RWing(SkoarToke):
    regex = re.compile(r"[)]\^\^")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_RWing)


class Toke_Segno(SkoarToke):
    regex = re.compile(r",[Ss](?:egno)?`(?:[a-zA-Z_][a-zA-Z0-9_]*`)*")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_Segno)


class Toke_Loco(SkoarToke):
    regex = re.compile(r"loco")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_Loco)


class Toke_Rep(SkoarToke):
    regex = re.compile(r"%+")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_Rep)


class Toke_Nosey(SkoarToke):
    regex = re.compile(r",")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_Nosey)


class Toke_LWing(SkoarToke):
    regex = re.compile(r"\^\^[(]")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_LWing)


class Toke_Deref(SkoarToke):
    regex = re.compile(r"!(?![!}]|=)")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_Deref)


class Toke_Meter(SkoarToke):
    regex = re.compile(r"[1-9][0-9]*/[1-9][0-9]*")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_Meter)


class Toke_DynFP(SkoarToke):
    regex = re.compile(r"fp")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_DynFP)


class Toke_LoopS(SkoarToke):
    regex = re.compile(r"[{]:[\n]*")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_LoopS)


class Toke_DynPiano(SkoarToke):
    regex = re.compile(r"(m(ezzo)?p|p+)(iano)?")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_DynPiano)


class Toke_SkoarpionStart(SkoarToke):
    regex = re.compile(r"[{]!")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_SkoarpionStart)


class Toke_DaCapo(SkoarToke):
    regex = re.compile(r"D\.C\.|Da Capo")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_DaCapo)


class Toke_SkoarpionSep(SkoarToke):
    regex = re.compile(r"!!")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_SkoarpionSep)


class Toke_Crotchets(SkoarToke):
    regex = re.compile(r"[}]+\.?")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_Crotchets)


class Toke_ListSep(SkoarToke):
    regex = re.compile(r",")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_ListSep)


class Toke_MsgName(SkoarToke):
    regex = re.compile(r"[a-zA-Z_][a-zA-Z0-9_]*(?!<)")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_MsgName)


class Toke_Comment(SkoarToke):
    regex = re.compile(r"<[?](.|[\n\r\f])*?[?]>")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_Comment)


class Toke_Bars(SkoarToke):
    regex = re.compile(r":?\|+:?")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_Bars)


class Toke_Quarters(SkoarToke):
    regex = re.compile(r"\.?[)]+(?:__?)?\.?")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_Quarters)


class Toke_Crap(SkoarToke):
    regex = re.compile(r"crap")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_Crap)


class Toke_ArgSpec(SkoarToke):
    regex = re.compile(r"<[a-zA-Z]+(,[a-zA-Z]+)*>")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_ArgSpec)


class Toke_Caesura(SkoarToke):
    regex = re.compile(r"//")

    @staticmethod
    def match(buf, offs):
        return SkoarToke.match_toke(buf, offs, Toke_Caesura)


