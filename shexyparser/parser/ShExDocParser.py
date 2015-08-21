# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .ShExDocVisitor import ShExDocVisitor
else:
    from ShExDocVisitor import ShExDocVisitor

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3C")
        buf.write("\u01cd\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\3\2\7\2j\n\2\f\2\16\2m\13\2\3\2\3\2\3\2\3\2\5\2s\n\2")
        buf.write("\3\2\7\2v\n\2\f\2\16\2y\13\2\5\2{\n\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\5\3\u0083\n\3\3\4\3\4\5\4\u0087\n\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\5\5\u008f\n\5\3\6\3\6\3\6\7\6\u0094\n\6")
        buf.write("\f\6\16\6\u0097\13\6\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00a9\n\n\3\13\5\13")
        buf.write("\u00ac\n\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\7\f\u00b5")
        buf.write("\n\f\f\f\16\f\u00b8\13\f\3\f\3\f\5\f\u00bc\n\f\3\f\3\f")
        buf.write("\3\r\3\r\6\r\u00c2\n\r\r\r\16\r\u00c3\3\16\3\16\6\16\u00c8")
        buf.write("\n\16\r\16\16\16\u00c9\3\17\3\17\3\17\7\17\u00cf\n\17")
        buf.write("\f\17\16\17\u00d2\13\17\3\20\3\20\3\20\7\20\u00d7\n\20")
        buf.write("\f\20\16\20\u00da\13\20\3\20\5\20\u00dd\n\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\5\21\u00e5\n\21\3\21\7\21\u00e8\n")
        buf.write("\21\f\21\16\21\u00eb\13\21\3\21\3\21\5\21\u00ef\n\21\3")
        buf.write("\22\3\22\3\22\3\23\3\23\5\23\u00f6\n\23\3\24\5\24\u00f9")
        buf.write("\n\24\3\24\3\24\3\24\5\24\u00fe\n\24\3\24\7\24\u0101\n")
        buf.write("\24\f\24\16\24\u0104\13\24\3\24\3\24\3\25\3\25\5\25\u010a")
        buf.write("\n\25\3\25\3\25\5\25\u010e\n\25\5\25\u0110\n\25\3\26\3")
        buf.write("\26\5\26\u0114\n\26\3\27\3\27\5\27\u0118\n\27\3\30\3\30")
        buf.write("\7\30\u011c\n\30\f\30\16\30\u011f\13\30\3\30\3\30\5\30")
        buf.write("\u0123\n\30\3\30\7\30\u0126\n\30\f\30\16\30\u0129\13\30")
        buf.write("\3\30\3\30\7\30\u012d\n\30\f\30\16\30\u0130\13\30\3\30")
        buf.write("\3\30\3\30\5\30\u0135\n\30\3\31\3\31\3\31\7\31\u013a\n")
        buf.write("\31\f\31\16\31\u013d\13\31\3\32\3\32\3\32\3\32\3\32\5")
        buf.write("\32\u0144\n\32\3\33\3\33\5\33\u0148\n\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\5\34\u0151\n\34\3\35\3\35\3\36\3")
        buf.write("\36\3\36\3\36\3\36\3\36\5\36\u015b\n\36\3\37\3\37\3 \3")
        buf.write(" \3!\3!\3\"\3\"\3\"\3\"\5\"\u0167\n\"\3#\3#\3#\3#\5#\u016d")
        buf.write("\n#\3$\3$\3$\3$\5$\u0173\n$\5$\u0175\n$\3$\3$\3%\3%\7")
        buf.write("%\u017b\n%\f%\16%\u017e\13%\3%\3%\3&\3&\5&\u0184\n&\3")
        buf.write("\'\3\'\3\'\7\'\u0189\n\'\f\'\16\'\u018c\13\'\5\'\u018e")
        buf.write("\n\'\3\'\3\'\6\'\u0192\n\'\r\'\16\'\u0193\5\'\u0196\n")
        buf.write("\'\3(\3(\3(\5(\u019b\n(\3)\3)\3)\5)\u01a0\n)\3*\3*\3+")
        buf.write("\3+\3+\3+\5+\u01a8\n+\3,\3,\3-\3-\3.\3.\5.\u01b0\n.\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\3\61\5\61\u01b9\n\61\3\61\5\61")
        buf.write("\u01bc\n\61\5\61\u01be\n\61\3\62\3\62\3\63\6\63\u01c3")
        buf.write("\n\63\r\63\16\63\u01c4\3\64\7\64\u01c8\n\64\f\64\16\64")
        buf.write("\u01cb\13\64\3\64\2\2\65\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`b")
        buf.write("df\2\13\4\2 !##\3\2*,\3\2&)\3\2-.\4\2\23\23<<\3\2<>\3")
        buf.write("\2/\60\3\2@C\3\2\66\67\u01e5\2k\3\2\2\2\4\u0082\3\2\2")
        buf.write("\2\6\u0086\3\2\2\2\b\u0088\3\2\2\2\n\u0090\3\2\2\2\f\u0098")
        buf.write("\3\2\2\2\16\u009b\3\2\2\2\20\u009e\3\2\2\2\22\u00a2\3")
        buf.write("\2\2\2\24\u00ab\3\2\2\2\26\u00b6\3\2\2\2\30\u00bf\3\2")
        buf.write("\2\2\32\u00c5\3\2\2\2\34\u00cb\3\2\2\2\36\u00d3\3\2\2")
        buf.write("\2 \u00ee\3\2\2\2\"\u00f0\3\2\2\2$\u00f5\3\2\2\2&\u00f8")
        buf.write("\3\2\2\2(\u010f\3\2\2\2*\u0113\3\2\2\2,\u0117\3\2\2\2")
        buf.write(".\u0134\3\2\2\2\60\u0136\3\2\2\2\62\u0143\3\2\2\2\64\u0147")
        buf.write("\3\2\2\2\66\u0150\3\2\2\28\u0152\3\2\2\2:\u015a\3\2\2")
        buf.write("\2<\u015c\3\2\2\2>\u015e\3\2\2\2@\u0160\3\2\2\2B\u0162")
        buf.write("\3\2\2\2D\u016c\3\2\2\2F\u016e\3\2\2\2H\u0178\3\2\2\2")
        buf.write("J\u0183\3\2\2\2L\u0195\3\2\2\2N\u0197\3\2\2\2P\u019f\3")
        buf.write("\2\2\2R\u01a1\3\2\2\2T\u01a3\3\2\2\2V\u01a9\3\2\2\2X\u01ab")
        buf.write("\3\2\2\2Z\u01af\3\2\2\2\\\u01b1\3\2\2\2^\u01b3\3\2\2\2")
        buf.write("`\u01b5\3\2\2\2b\u01bf\3\2\2\2d\u01c2\3\2\2\2f\u01c9\3")
        buf.write("\2\2\2hj\5\6\4\2ih\3\2\2\2jm\3\2\2\2ki\3\2\2\2kl\3\2\2")
        buf.write("\2lz\3\2\2\2mk\3\2\2\2ns\5\24\13\2os\5\22\n\2ps\5\b\5")
        buf.write("\2qs\5d\63\2rn\3\2\2\2ro\3\2\2\2rp\3\2\2\2rq\3\2\2\2s")
        buf.write("w\3\2\2\2tv\5\4\3\2ut\3\2\2\2vy\3\2\2\2wu\3\2\2\2wx\3")
        buf.write("\2\2\2x{\3\2\2\2yw\3\2\2\2zr\3\2\2\2z{\3\2\2\2{|\3\2\2")
        buf.write("\2|}\7\2\2\3}\3\3\2\2\2~\u0083\5\6\4\2\177\u0083\5\22")
        buf.write("\n\2\u0080\u0083\5\24\13\2\u0081\u0083\5\b\5\2\u0082~")
        buf.write("\3\2\2\2\u0082\177\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0081")
        buf.write("\3\2\2\2\u0083\5\3\2\2\2\u0084\u0087\5\16\b\2\u0085\u0087")
        buf.write("\5\20\t\2\u0086\u0084\3\2\2\2\u0086\u0085\3\2\2\2\u0087")
        buf.write("\7\3\2\2\2\u0088\u008e\5\f\7\2\u0089\u008a\7\3\2\2\u008a")
        buf.write("\u008b\5\n\6\2\u008b\u008c\5f\64\2\u008c\u008f\3\2\2\2")
        buf.write("\u008d\u008f\7\31\2\2\u008e\u0089\3\2\2\2\u008e\u008d")
        buf.write("\3\2\2\2\u008f\t\3\2\2\2\u0090\u0095\5.\30\2\u0091\u0092")
        buf.write("\7\4\2\2\u0092\u0094\5.\30\2\u0093\u0091\3\2\2\2\u0094")
        buf.write("\u0097\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0096\3\2\2\2")
        buf.write("\u0096\13\3\2\2\2\u0097\u0095\3\2\2\2\u0098\u0099\7\5")
        buf.write("\2\2\u0099\u009a\5Z.\2\u009a\r\3\2\2\2\u009b\u009c\7\30")
        buf.write("\2\2\u009c\u009d\7\65\2\2\u009d\17\3\2\2\2\u009e\u009f")
        buf.write("\7\32\2\2\u009f\u00a0\7\66\2\2\u00a0\u00a1\7\65\2\2\u00a1")
        buf.write("\21\3\2\2\2\u00a2\u00a3\7\33\2\2\u00a3\u00a8\7\3\2\2\u00a4")
        buf.write("\u00a9\5$\23\2\u00a5\u00a6\5\26\f\2\u00a6\u00a7\5f\64")
        buf.write("\2\u00a7\u00a9\3\2\2\2\u00a8\u00a4\3\2\2\2\u00a8\u00a5")
        buf.write("\3\2\2\2\u00a9\23\3\2\2\2\u00aa\u00ac\7\34\2\2\u00ab\u00aa")
        buf.write("\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad")
        buf.write("\u00ae\5$\23\2\u00ae\u00af\5\26\f\2\u00af\u00b0\5f\64")
        buf.write("\2\u00b0\25\3\2\2\2\u00b1\u00b5\5\30\r\2\u00b2\u00b5\5")
        buf.write("\32\16\2\u00b3\u00b5\7\35\2\2\u00b4\u00b1\3\2\2\2\u00b4")
        buf.write("\u00b2\3\2\2\2\u00b4\u00b3\3\2\2\2\u00b5\u00b8\3\2\2\2")
        buf.write("\u00b6\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b9\3")
        buf.write("\2\2\2\u00b8\u00b6\3\2\2\2\u00b9\u00bb\7\6\2\2\u00ba\u00bc")
        buf.write("\5\34\17\2\u00bb\u00ba\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc")
        buf.write("\u00bd\3\2\2\2\u00bd\u00be\7\7\2\2\u00be\27\3\2\2\2\u00bf")
        buf.write("\u00c1\7\b\2\2\u00c0\u00c2\5$\23\2\u00c1\u00c0\3\2\2\2")
        buf.write("\u00c2\u00c3\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c3\u00c4\3")
        buf.write("\2\2\2\u00c4\31\3\2\2\2\u00c5\u00c7\7\36\2\2\u00c6\u00c8")
        buf.write("\5*\26\2\u00c7\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9")
        buf.write("\u00c7\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\33\3\2\2\2\u00cb")
        buf.write("\u00d0\5\36\20\2\u00cc\u00cd\7\t\2\2\u00cd\u00cf\5\36")
        buf.write("\20\2\u00ce\u00cc\3\2\2\2\u00cf\u00d2\3\2\2\2\u00d0\u00ce")
        buf.write("\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\35\3\2\2\2\u00d2\u00d0")
        buf.write("\3\2\2\2\u00d3\u00d8\5 \21\2\u00d4\u00d5\7\n\2\2\u00d5")
        buf.write("\u00d7\5 \21\2\u00d6\u00d4\3\2\2\2\u00d7\u00da\3\2\2\2")
        buf.write("\u00d8\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00dc\3")
        buf.write("\2\2\2\u00da\u00d8\3\2\2\2\u00db\u00dd\7\n\2\2\u00dc\u00db")
        buf.write("\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\37\3\2\2\2\u00de\u00ef")
        buf.write("\5&\24\2\u00df\u00ef\5\"\22\2\u00e0\u00e1\7\13\2\2\u00e1")
        buf.write("\u00e2\5\34\17\2\u00e2\u00e4\7\f\2\2\u00e3\u00e5\5D#\2")
        buf.write("\u00e4\u00e3\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e9\3")
        buf.write("\2\2\2\u00e6\u00e8\5B\"\2\u00e7\u00e6\3\2\2\2\u00e8\u00eb")
        buf.write("\3\2\2\2\u00e9\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea")
        buf.write("\u00ec\3\2\2\2\u00eb\u00e9\3\2\2\2\u00ec\u00ed\5f\64\2")
        buf.write("\u00ed\u00ef\3\2\2\2\u00ee\u00de\3\2\2\2\u00ee\u00df\3")
        buf.write("\2\2\2\u00ee\u00e0\3\2\2\2\u00ef!\3\2\2\2\u00f0\u00f1")
        buf.write("\7\b\2\2\u00f1\u00f2\5$\23\2\u00f2#\3\2\2\2\u00f3\u00f6")
        buf.write("\5Z.\2\u00f4\u00f6\5^\60\2\u00f5\u00f3\3\2\2\2\u00f5\u00f4")
        buf.write("\3\2\2\2\u00f6%\3\2\2\2\u00f7\u00f9\5(\25\2\u00f8\u00f7")
        buf.write("\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa")
        buf.write("\u00fb\5*\26\2\u00fb\u00fd\5,\27\2\u00fc\u00fe\5D#\2\u00fd")
        buf.write("\u00fc\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u0102\3\2\2\2")
        buf.write("\u00ff\u0101\5B\"\2\u0100\u00ff\3\2\2\2\u0101\u0104\3")
        buf.write("\2\2\2\u0102\u0100\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u0105")
        buf.write("\3\2\2\2\u0104\u0102\3\2\2\2\u0105\u0106\5f\64\2\u0106")
        buf.write("\'\3\2\2\2\u0107\u0109\7\r\2\2\u0108\u010a\7\16\2\2\u0109")
        buf.write("\u0108\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u0110\3\2\2\2")
        buf.write("\u010b\u010d\7\16\2\2\u010c\u010e\7\r\2\2\u010d\u010c")
        buf.write("\3\2\2\2\u010d\u010e\3\2\2\2\u010e\u0110\3\2\2\2\u010f")
        buf.write("\u0107\3\2\2\2\u010f\u010b\3\2\2\2\u0110)\3\2\2\2\u0111")
        buf.write("\u0114\5Z.\2\u0112\u0114\7\64\2\2\u0113\u0111\3\2\2\2")
        buf.write("\u0113\u0112\3\2\2\2\u0114+\3\2\2\2\u0115\u0118\5.\30")
        buf.write("\2\u0116\u0118\5\f\7\2\u0117\u0115\3\2\2\2\u0117\u0116")
        buf.write("\3\2\2\2\u0118-\3\2\2\2\u0119\u011d\7\37\2\2\u011a\u011c")
        buf.write("\5\64\33\2\u011b\u011a\3\2\2\2\u011c\u011f\3\2\2\2\u011d")
        buf.write("\u011b\3\2\2\2\u011d\u011e\3\2\2\2\u011e\u0135\3\2\2\2")
        buf.write("\u011f\u011d\3\2\2\2\u0120\u0122\t\2\2\2\u0121\u0123\5")
        buf.write("\60\31\2\u0122\u0121\3\2\2\2\u0122\u0123\3\2\2\2\u0123")
        buf.write("\u0127\3\2\2\2\u0124\u0126\5\66\34\2\u0125\u0124\3\2\2")
        buf.write("\2\u0126\u0129\3\2\2\2\u0127\u0125\3\2\2\2\u0127\u0128")
        buf.write("\3\2\2\2\u0128\u0135\3\2\2\2\u0129\u0127\3\2\2\2\u012a")
        buf.write("\u012e\5@!\2\u012b\u012d\5\64\33\2\u012c\u012b\3\2\2\2")
        buf.write("\u012d\u0130\3\2\2\2\u012e\u012c\3\2\2\2\u012e\u012f\3")
        buf.write("\2\2\2\u012f\u0135\3\2\2\2\u0130\u012e\3\2\2\2\u0131\u0135")
        buf.write("\5\60\31\2\u0132\u0135\5H%\2\u0133\u0135\7\17\2\2\u0134")
        buf.write("\u0119\3\2\2\2\u0134\u0120\3\2\2\2\u0134\u012a\3\2\2\2")
        buf.write("\u0134\u0131\3\2\2\2\u0134\u0132\3\2\2\2\u0134\u0133\3")
        buf.write("\2\2\2\u0135/\3\2\2\2\u0136\u013b\5\62\32\2\u0137\u0138")
        buf.write("\7%\2\2\u0138\u013a\5\62\32\2\u0139\u0137\3\2\2\2\u013a")
        buf.write("\u013d\3\2\2\2\u013b\u0139\3\2\2\2\u013b\u013c\3\2\2\2")
        buf.write("\u013c\61\3\2\2\2\u013d\u013b\3\2\2\2\u013e\u0144\79\2")
        buf.write("\2\u013f\u0144\78\2\2\u0140\u0141\7\20\2\2\u0141\u0144")
        buf.write("\5$\23\2\u0142\u0144\5\26\f\2\u0143\u013e\3\2\2\2\u0143")
        buf.write("\u013f\3\2\2\2\u0143\u0140\3\2\2\2\u0143\u0142\3\2\2\2")
        buf.write("\u0144\63\3\2\2\2\u0145\u0148\5\66\34\2\u0146\u0148\5")
        buf.write(":\36\2\u0147\u0145\3\2\2\2\u0147\u0146\3\2\2\2\u0148\65")
        buf.write("\3\2\2\2\u0149\u014a\58\35\2\u014a\u014b\7<\2\2\u014b")
        buf.write("\u0151\3\2\2\2\u014c\u014d\7\"\2\2\u014d\u0151\5X-\2\u014e")
        buf.write("\u014f\7\21\2\2\u014f\u0151\5X-\2\u0150\u0149\3\2\2\2")
        buf.write("\u0150\u014c\3\2\2\2\u0150\u014e\3\2\2\2\u0151\67\3\2")
        buf.write("\2\2\u0152\u0153\t\3\2\2\u01539\3\2\2\2\u0154\u0155\5")
        buf.write("<\37\2\u0155\u0156\7<\2\2\u0156\u015b\3\2\2\2\u0157\u0158")
        buf.write("\5> \2\u0158\u0159\7<\2\2\u0159\u015b\3\2\2\2\u015a\u0154")
        buf.write("\3\2\2\2\u015a\u0157\3\2\2\2\u015b;\3\2\2\2\u015c\u015d")
        buf.write("\t\4\2\2\u015d=\3\2\2\2\u015e\u015f\t\5\2\2\u015f?\3\2")
        buf.write("\2\2\u0160\u0161\5Z.\2\u0161A\3\2\2\2\u0162\u0163\7\22")
        buf.write("\2\2\u0163\u0166\5Z.\2\u0164\u0167\5Z.\2\u0165\u0167\5")
        buf.write("P)\2\u0166\u0164\3\2\2\2\u0166\u0165\3\2\2\2\u0167C\3")
        buf.write("\2\2\2\u0168\u016d\7\23\2\2\u0169\u016d\7\4\2\2\u016a")
        buf.write("\u016d\7\24\2\2\u016b\u016d\5F$\2\u016c\u0168\3\2\2\2")
        buf.write("\u016c\u0169\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016b\3")
        buf.write("\2\2\2\u016dE\3\2\2\2\u016e\u016f\7\6\2\2\u016f\u0174")
        buf.write("\7<\2\2\u0170\u0172\7\n\2\2\u0171\u0173\t\6\2\2\u0172")
        buf.write("\u0171\3\2\2\2\u0172\u0173\3\2\2\2\u0173\u0175\3\2\2\2")
        buf.write("\u0174\u0170\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0176\3")
        buf.write("\2\2\2\u0176\u0177\7\7\2\2\u0177G\3\2\2\2\u0178\u017c")
        buf.write("\7\13\2\2\u0179\u017b\5J&\2\u017a\u0179\3\2\2\2\u017b")
        buf.write("\u017e\3\2\2\2\u017c\u017a\3\2\2\2\u017c\u017d\3\2\2\2")
        buf.write("\u017d\u017f\3\2\2\2\u017e\u017c\3\2\2\2\u017f\u0180\7")
        buf.write("\f\2\2\u0180I\3\2\2\2\u0181\u0184\5L\'\2\u0182\u0184\5")
        buf.write("P)\2\u0183\u0181\3\2\2\2\u0183\u0182\3\2\2\2\u0184K\3")
        buf.write("\2\2\2\u0185\u018d\5Z.\2\u0186\u018a\7\21\2\2\u0187\u0189")
        buf.write("\5N(\2\u0188\u0187\3\2\2\2\u0189\u018c\3\2\2\2\u018a\u0188")
        buf.write("\3\2\2\2\u018a\u018b\3\2\2\2\u018b\u018e\3\2\2\2\u018c")
        buf.write("\u018a\3\2\2\2\u018d\u0186\3\2\2\2\u018d\u018e\3\2\2\2")
        buf.write("\u018e\u0196\3\2\2\2\u018f\u0191\7\17\2\2\u0190\u0192")
        buf.write("\5N(\2\u0191\u0190\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0191")
        buf.write("\3\2\2\2\u0193\u0194\3\2\2\2\u0194\u0196\3\2\2\2\u0195")
        buf.write("\u0185\3\2\2\2\u0195\u018f\3\2\2\2\u0196M\3\2\2\2\u0197")
        buf.write("\u0198\7\25\2\2\u0198\u019a\5Z.\2\u0199\u019b\7\21\2\2")
        buf.write("\u019a\u0199\3\2\2\2\u019a\u019b\3\2\2\2\u019bO\3\2\2")
        buf.write("\2\u019c\u01a0\5T+\2\u019d\u01a0\5R*\2\u019e\u01a0\5V")
        buf.write(",\2\u019f\u019c\3\2\2\2\u019f\u019d\3\2\2\2\u019f\u019e")
        buf.write("\3\2\2\2\u01a0Q\3\2\2\2\u01a1\u01a2\t\7\2\2\u01a2S\3\2")
        buf.write("\2\2\u01a3\u01a7\5X-\2\u01a4\u01a8\7;\2\2\u01a5\u01a6")
        buf.write("\7\26\2\2\u01a6\u01a8\5@!\2\u01a7\u01a4\3\2\2\2\u01a7")
        buf.write("\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8U\3\2\2\2\u01a9")
        buf.write("\u01aa\t\b\2\2\u01aaW\3\2\2\2\u01ab\u01ac\t\t\2\2\u01ac")
        buf.write("Y\3\2\2\2\u01ad\u01b0\7\65\2\2\u01ae\u01b0\5\\/\2\u01af")
        buf.write("\u01ad\3\2\2\2\u01af\u01ae\3\2\2\2\u01b0[\3\2\2\2\u01b1")
        buf.write("\u01b2\t\n\2\2\u01b2]\3\2\2\2\u01b3\u01b4\7:\2\2\u01b4")
        buf.write("_\3\2\2\2\u01b5\u01bd\7\27\2\2\u01b6\u01be\5b\62\2\u01b7")
        buf.write("\u01b9\5Z.\2\u01b8\u01b7\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9")
        buf.write("\u01bb\3\2\2\2\u01ba\u01bc\7\63\2\2\u01bb\u01ba\3\2\2")
        buf.write("\2\u01bb\u01bc\3\2\2\2\u01bc\u01be\3\2\2\2\u01bd\u01b6")
        buf.write("\3\2\2\2\u01bd\u01b8\3\2\2\2\u01bea\3\2\2\2\u01bf\u01c0")
        buf.write("\7?\2\2\u01c0c\3\2\2\2\u01c1\u01c3\5`\61\2\u01c2\u01c1")
        buf.write("\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4")
        buf.write("\u01c5\3\2\2\2\u01c5e\3\2\2\2\u01c6\u01c8\5`\61\2\u01c7")
        buf.write("\u01c6\3\2\2\2\u01c8\u01cb\3\2\2\2\u01c9\u01c7\3\2\2\2")
        buf.write("\u01c9\u01ca\3\2\2\2\u01cag\3\2\2\2\u01cb\u01c9\3\2\2")
        buf.write("\2=krwz\u0082\u0086\u008e\u0095\u00a8\u00ab\u00b4\u00b6")
        buf.write("\u00bb\u00c3\u00c9\u00d0\u00d8\u00dc\u00e4\u00e9\u00ee")
        buf.write("\u00f5\u00f8\u00fd\u0102\u0109\u010d\u010f\u0113\u0117")
        buf.write("\u011d\u0122\u0127\u012e\u0134\u013b\u0143\u0147\u0150")
        buf.write("\u015a\u0166\u016c\u0172\u0174\u017c\u0183\u018a\u018d")
        buf.write("\u0193\u0195\u019a\u019f\u01a7\u01af\u01b8\u01bb\u01bd")
        buf.write("\u01c4\u01c9")
        return buf.getvalue()


class ShExDocParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'='", u"'+'", u"'$'", u"'{'", u"'}'", 
                     u"'&'", u"'|'", u"','", u"'('", u"')'", u"'!'", u"'^'", 
                     u"'.'", u"'@'", u"'~'", u"';'", u"'*'", u"'?'", u"'-'", 
                     u"'^^'", u"'%'", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"'true'", u"'false'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"KW_BASE", u"KW_EXTERNAL", 
                      u"KW_PREFIX", u"KW_START", u"KW_VIRTUAL", u"KW_CLOSED", 
                      u"KW_EXTRA", u"KW_LITERAL", u"KW_IRI", u"KW_NONLITERAL", 
                      u"KW_PATTERN", u"KW_BNODE", u"KW_AND", u"KW_OR", u"KW_MININCLUSIVE", 
                      u"KW_MINEXCLUSIVE", u"KW_MAXINCLUSIVE", u"KW_MAXEXCLUSIVE", 
                      u"KW_LENGTH", u"KW_MINLENGTH", u"KW_MAXLENGTH", u"KW_TOTALDIGITS", 
                      u"KW_FRACTIONDIGITS", u"KW_TRUE", u"KW_FALSE", u"PASS", 
                      u"COMMENT", u"CODE", u"RDF_TYPE", u"IRIREF", u"PNAME_NS", 
                      u"PNAME_LN", u"ATPNAME_NS", u"ATPNAME_LN", u"BLANK_NODE_LABEL", 
                      u"LANGTAG", u"INTEGER", u"DECIMAL", u"DOUBLE", u"UCASE_LABEL", 
                      u"STRING_LITERAL1", u"STRING_LITERAL2", u"STRING_LITERAL_LONG1", 
                      u"STRING_LITERAL_LONG2" ]

    RULE_shExDoc = 0
    RULE_statement = 1
    RULE_directive = 2
    RULE_valueClassDefinition = 3
    RULE_valueClassExpr = 4
    RULE_valueClassLabel = 5
    RULE_baseDecl = 6
    RULE_prefixDecl = 7
    RULE_start = 8
    RULE_shape = 9
    RULE_shapeDefinition = 10
    RULE_includeSet = 11
    RULE_inclPropertySet = 12
    RULE_someOfShape = 13
    RULE_groupShape = 14
    RULE_unaryShape = 15
    RULE_include = 16
    RULE_shapeLabel = 17
    RULE_tripleConstraint = 18
    RULE_senseFlags = 19
    RULE_predicate = 20
    RULE_valueClassOrRef = 21
    RULE_valueClass = 22
    RULE_groupShapeConstr = 23
    RULE_shapeOrRef = 24
    RULE_xsFacet = 25
    RULE_stringFacet = 26
    RULE_stringLength = 27
    RULE_numericFacet = 28
    RULE_numericRange = 29
    RULE_numericLength = 30
    RULE_datatype = 31
    RULE_annotation = 32
    RULE_cardinality = 33
    RULE_repeatRange = 34
    RULE_valueSet = 35
    RULE_value = 36
    RULE_iriRange = 37
    RULE_exclusion = 38
    RULE_literal = 39
    RULE_numericLiteral = 40
    RULE_rdfLiteral = 41
    RULE_booleanLiteral = 42
    RULE_string = 43
    RULE_iri = 44
    RULE_prefixedName = 45
    RULE_blankNode = 46
    RULE_codeDecl = 47
    RULE_codeLabel = 48
    RULE_startActions = 49
    RULE_semanticActions = 50

    ruleNames =  [ "shExDoc", "statement", "directive", "valueClassDefinition", 
                   "valueClassExpr", "valueClassLabel", "baseDecl", "prefixDecl", 
                   "start", "shape", "shapeDefinition", "includeSet", "inclPropertySet", 
                   "someOfShape", "groupShape", "unaryShape", "include", 
                   "shapeLabel", "tripleConstraint", "senseFlags", "predicate", 
                   "valueClassOrRef", "valueClass", "groupShapeConstr", 
                   "shapeOrRef", "xsFacet", "stringFacet", "stringLength", 
                   "numericFacet", "numericRange", "numericLength", "datatype", 
                   "annotation", "cardinality", "repeatRange", "valueSet", 
                   "value", "iriRange", "exclusion", "literal", "numericLiteral", 
                   "rdfLiteral", "booleanLiteral", "string", "iri", "prefixedName", 
                   "blankNode", "codeDecl", "codeLabel", "startActions", 
                   "semanticActions" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    KW_BASE=22
    KW_EXTERNAL=23
    KW_PREFIX=24
    KW_START=25
    KW_VIRTUAL=26
    KW_CLOSED=27
    KW_EXTRA=28
    KW_LITERAL=29
    KW_IRI=30
    KW_NONLITERAL=31
    KW_PATTERN=32
    KW_BNODE=33
    KW_AND=34
    KW_OR=35
    KW_MININCLUSIVE=36
    KW_MINEXCLUSIVE=37
    KW_MAXINCLUSIVE=38
    KW_MAXEXCLUSIVE=39
    KW_LENGTH=40
    KW_MINLENGTH=41
    KW_MAXLENGTH=42
    KW_TOTALDIGITS=43
    KW_FRACTIONDIGITS=44
    KW_TRUE=45
    KW_FALSE=46
    PASS=47
    COMMENT=48
    CODE=49
    RDF_TYPE=50
    IRIREF=51
    PNAME_NS=52
    PNAME_LN=53
    ATPNAME_NS=54
    ATPNAME_LN=55
    BLANK_NODE_LABEL=56
    LANGTAG=57
    INTEGER=58
    DECIMAL=59
    DOUBLE=60
    UCASE_LABEL=61
    STRING_LITERAL1=62
    STRING_LITERAL2=63
    STRING_LITERAL_LONG1=64
    STRING_LITERAL_LONG2=65

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ShExDocContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ShExDocParser.EOF, 0)

        def directive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShExDocParser.DirectiveContext)
            else:
                return self.getTypedRuleContext(ShExDocParser.DirectiveContext,i)


        def shape(self):
            return self.getTypedRuleContext(ShExDocParser.ShapeContext,0)


        def start(self):
            return self.getTypedRuleContext(ShExDocParser.StartContext,0)


        def valueClassDefinition(self):
            return self.getTypedRuleContext(ShExDocParser.ValueClassDefinitionContext,0)


        def startActions(self):
            return self.getTypedRuleContext(ShExDocParser.StartActionsContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShExDocParser.StatementContext)
            else:
                return self.getTypedRuleContext(ShExDocParser.StatementContext,i)


        def getRuleIndex(self):
            return ShExDocParser.RULE_shExDoc

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitShExDoc(self)
            else:
                return visitor.visitChildren(self)




    def shExDoc(self):

        localctx = ShExDocParser.ShExDocContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_shExDoc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ShExDocParser.KW_BASE or _la==ShExDocParser.KW_PREFIX:
                self.state = 102
                self.directive()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 120
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ShExDocParser.T__2) | (1 << ShExDocParser.T__20) | (1 << ShExDocParser.KW_START) | (1 << ShExDocParser.KW_VIRTUAL) | (1 << ShExDocParser.IRIREF) | (1 << ShExDocParser.PNAME_NS) | (1 << ShExDocParser.PNAME_LN) | (1 << ShExDocParser.BLANK_NODE_LABEL))) != 0):
                self.state = 112
                token = self._input.LA(1)
                if token in [ShExDocParser.KW_VIRTUAL, ShExDocParser.IRIREF, ShExDocParser.PNAME_NS, ShExDocParser.PNAME_LN, ShExDocParser.BLANK_NODE_LABEL]:
                    self.state = 108
                    self.shape()

                elif token in [ShExDocParser.KW_START]:
                    self.state = 109
                    self.start()

                elif token in [ShExDocParser.T__2]:
                    self.state = 110
                    self.valueClassDefinition()

                elif token in [ShExDocParser.T__20]:
                    self.state = 111
                    self.startActions()

                else:
                    raise NoViableAltException(self)

                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ShExDocParser.T__2) | (1 << ShExDocParser.KW_BASE) | (1 << ShExDocParser.KW_PREFIX) | (1 << ShExDocParser.KW_START) | (1 << ShExDocParser.KW_VIRTUAL) | (1 << ShExDocParser.IRIREF) | (1 << ShExDocParser.PNAME_NS) | (1 << ShExDocParser.PNAME_LN) | (1 << ShExDocParser.BLANK_NODE_LABEL))) != 0):
                    self.state = 114
                    self.statement()
                    self.state = 119
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 122
            self.match(ShExDocParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def directive(self):
            return self.getTypedRuleContext(ShExDocParser.DirectiveContext,0)


        def start(self):
            return self.getTypedRuleContext(ShExDocParser.StartContext,0)


        def shape(self):
            return self.getTypedRuleContext(ShExDocParser.ShapeContext,0)


        def valueClassDefinition(self):
            return self.getTypedRuleContext(ShExDocParser.ValueClassDefinitionContext,0)


        def getRuleIndex(self):
            return ShExDocParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ShExDocParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 128
            token = self._input.LA(1)
            if token in [ShExDocParser.KW_BASE, ShExDocParser.KW_PREFIX]:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.directive()

            elif token in [ShExDocParser.KW_START]:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.start()

            elif token in [ShExDocParser.KW_VIRTUAL, ShExDocParser.IRIREF, ShExDocParser.PNAME_NS, ShExDocParser.PNAME_LN, ShExDocParser.BLANK_NODE_LABEL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.shape()

            elif token in [ShExDocParser.T__2]:
                self.enterOuterAlt(localctx, 4)
                self.state = 127
                self.valueClassDefinition()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DirectiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def baseDecl(self):
            return self.getTypedRuleContext(ShExDocParser.BaseDeclContext,0)


        def prefixDecl(self):
            return self.getTypedRuleContext(ShExDocParser.PrefixDeclContext,0)


        def getRuleIndex(self):
            return ShExDocParser.RULE_directive

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitDirective(self)
            else:
                return visitor.visitChildren(self)




    def directive(self):

        localctx = ShExDocParser.DirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_directive)
        try:
            self.state = 132
            token = self._input.LA(1)
            if token in [ShExDocParser.KW_BASE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.baseDecl()

            elif token in [ShExDocParser.KW_PREFIX]:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.prefixDecl()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueClassDefinitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def valueClassLabel(self):
            return self.getTypedRuleContext(ShExDocParser.ValueClassLabelContext,0)


        def valueClassExpr(self):
            return self.getTypedRuleContext(ShExDocParser.ValueClassExprContext,0)


        def semanticActions(self):
            return self.getTypedRuleContext(ShExDocParser.SemanticActionsContext,0)


        def KW_EXTERNAL(self):
            return self.getToken(ShExDocParser.KW_EXTERNAL, 0)

        def getRuleIndex(self):
            return ShExDocParser.RULE_valueClassDefinition

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitValueClassDefinition(self)
            else:
                return visitor.visitChildren(self)




    def valueClassDefinition(self):

        localctx = ShExDocParser.ValueClassDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_valueClassDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.valueClassLabel()
            self.state = 140
            token = self._input.LA(1)
            if token in [ShExDocParser.T__0]:
                self.state = 135
                self.match(ShExDocParser.T__0)
                self.state = 136
                self.valueClassExpr()
                self.state = 137
                self.semanticActions()

            elif token in [ShExDocParser.KW_EXTERNAL]:
                self.state = 139
                self.match(ShExDocParser.KW_EXTERNAL)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueClassExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def valueClass(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShExDocParser.ValueClassContext)
            else:
                return self.getTypedRuleContext(ShExDocParser.ValueClassContext,i)


        def getRuleIndex(self):
            return ShExDocParser.RULE_valueClassExpr

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitValueClassExpr(self)
            else:
                return visitor.visitChildren(self)




    def valueClassExpr(self):

        localctx = ShExDocParser.ValueClassExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_valueClassExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.valueClass()
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ShExDocParser.T__1:
                self.state = 143
                self.match(ShExDocParser.T__1)
                self.state = 144
                self.valueClass()
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueClassLabelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def iri(self):
            return self.getTypedRuleContext(ShExDocParser.IriContext,0)


        def getRuleIndex(self):
            return ShExDocParser.RULE_valueClassLabel

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitValueClassLabel(self)
            else:
                return visitor.visitChildren(self)




    def valueClassLabel(self):

        localctx = ShExDocParser.ValueClassLabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_valueClassLabel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(ShExDocParser.T__2)
            self.state = 151
            self.iri()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BaseDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_BASE(self):
            return self.getToken(ShExDocParser.KW_BASE, 0)

        def IRIREF(self):
            return self.getToken(ShExDocParser.IRIREF, 0)

        def getRuleIndex(self):
            return ShExDocParser.RULE_baseDecl

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitBaseDecl(self)
            else:
                return visitor.visitChildren(self)




    def baseDecl(self):

        localctx = ShExDocParser.BaseDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_baseDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(ShExDocParser.KW_BASE)
            self.state = 154
            self.match(ShExDocParser.IRIREF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrefixDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_PREFIX(self):
            return self.getToken(ShExDocParser.KW_PREFIX, 0)

        def PNAME_NS(self):
            return self.getToken(ShExDocParser.PNAME_NS, 0)

        def IRIREF(self):
            return self.getToken(ShExDocParser.IRIREF, 0)

        def getRuleIndex(self):
            return ShExDocParser.RULE_prefixDecl

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitPrefixDecl(self)
            else:
                return visitor.visitChildren(self)




    def prefixDecl(self):

        localctx = ShExDocParser.PrefixDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_prefixDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(ShExDocParser.KW_PREFIX)
            self.state = 157
            self.match(ShExDocParser.PNAME_NS)
            self.state = 158
            self.match(ShExDocParser.IRIREF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_START(self):
            return self.getToken(ShExDocParser.KW_START, 0)

        def shapeLabel(self):
            return self.getTypedRuleContext(ShExDocParser.ShapeLabelContext,0)


        def shapeDefinition(self):
            return self.getTypedRuleContext(ShExDocParser.ShapeDefinitionContext,0)


        def semanticActions(self):
            return self.getTypedRuleContext(ShExDocParser.SemanticActionsContext,0)


        def getRuleIndex(self):
            return ShExDocParser.RULE_start

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = ShExDocParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(ShExDocParser.KW_START)
            self.state = 161
            self.match(ShExDocParser.T__0)
            self.state = 166
            token = self._input.LA(1)
            if token in [ShExDocParser.IRIREF, ShExDocParser.PNAME_NS, ShExDocParser.PNAME_LN, ShExDocParser.BLANK_NODE_LABEL]:
                self.state = 162
                self.shapeLabel()

            elif token in [ShExDocParser.T__3, ShExDocParser.T__5, ShExDocParser.KW_CLOSED, ShExDocParser.KW_EXTRA]:
                self.state = 163
                self.shapeDefinition()
                self.state = 164
                self.semanticActions()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ShapeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def shapeLabel(self):
            return self.getTypedRuleContext(ShExDocParser.ShapeLabelContext,0)


        def shapeDefinition(self):
            return self.getTypedRuleContext(ShExDocParser.ShapeDefinitionContext,0)


        def semanticActions(self):
            return self.getTypedRuleContext(ShExDocParser.SemanticActionsContext,0)


        def KW_VIRTUAL(self):
            return self.getToken(ShExDocParser.KW_VIRTUAL, 0)

        def getRuleIndex(self):
            return ShExDocParser.RULE_shape

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitShape(self)
            else:
                return visitor.visitChildren(self)




    def shape(self):

        localctx = ShExDocParser.ShapeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_shape)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            _la = self._input.LA(1)
            if _la==ShExDocParser.KW_VIRTUAL:
                self.state = 168
                self.match(ShExDocParser.KW_VIRTUAL)


            self.state = 171
            self.shapeLabel()
            self.state = 172
            self.shapeDefinition()
            self.state = 173
            self.semanticActions()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ShapeDefinitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def includeSet(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShExDocParser.IncludeSetContext)
            else:
                return self.getTypedRuleContext(ShExDocParser.IncludeSetContext,i)


        def inclPropertySet(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShExDocParser.InclPropertySetContext)
            else:
                return self.getTypedRuleContext(ShExDocParser.InclPropertySetContext,i)


        def KW_CLOSED(self, i:int=None):
            if i is None:
                return self.getTokens(ShExDocParser.KW_CLOSED)
            else:
                return self.getToken(ShExDocParser.KW_CLOSED, i)

        def someOfShape(self):
            return self.getTypedRuleContext(ShExDocParser.SomeOfShapeContext,0)


        def getRuleIndex(self):
            return ShExDocParser.RULE_shapeDefinition

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitShapeDefinition(self)
            else:
                return visitor.visitChildren(self)




    def shapeDefinition(self):

        localctx = ShExDocParser.ShapeDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_shapeDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ShExDocParser.T__5) | (1 << ShExDocParser.KW_CLOSED) | (1 << ShExDocParser.KW_EXTRA))) != 0):
                self.state = 178
                token = self._input.LA(1)
                if token in [ShExDocParser.T__5]:
                    self.state = 175
                    self.includeSet()

                elif token in [ShExDocParser.KW_EXTRA]:
                    self.state = 176
                    self.inclPropertySet()

                elif token in [ShExDocParser.KW_CLOSED]:
                    self.state = 177
                    self.match(ShExDocParser.KW_CLOSED)

                else:
                    raise NoViableAltException(self)

                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 183
            self.match(ShExDocParser.T__3)
            self.state = 185
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ShExDocParser.T__5) | (1 << ShExDocParser.T__8) | (1 << ShExDocParser.T__10) | (1 << ShExDocParser.T__11) | (1 << ShExDocParser.RDF_TYPE) | (1 << ShExDocParser.IRIREF) | (1 << ShExDocParser.PNAME_NS) | (1 << ShExDocParser.PNAME_LN))) != 0):
                self.state = 184
                self.someOfShape()


            self.state = 187
            self.match(ShExDocParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IncludeSetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def shapeLabel(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShExDocParser.ShapeLabelContext)
            else:
                return self.getTypedRuleContext(ShExDocParser.ShapeLabelContext,i)


        def getRuleIndex(self):
            return ShExDocParser.RULE_includeSet

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitIncludeSet(self)
            else:
                return visitor.visitChildren(self)




    def includeSet(self):

        localctx = ShExDocParser.IncludeSetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_includeSet)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(ShExDocParser.T__5)
            self.state = 191 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 190
                self.shapeLabel()
                self.state = 193 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ShExDocParser.IRIREF) | (1 << ShExDocParser.PNAME_NS) | (1 << ShExDocParser.PNAME_LN) | (1 << ShExDocParser.BLANK_NODE_LABEL))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InclPropertySetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_EXTRA(self):
            return self.getToken(ShExDocParser.KW_EXTRA, 0)

        def predicate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShExDocParser.PredicateContext)
            else:
                return self.getTypedRuleContext(ShExDocParser.PredicateContext,i)


        def getRuleIndex(self):
            return ShExDocParser.RULE_inclPropertySet

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitInclPropertySet(self)
            else:
                return visitor.visitChildren(self)




    def inclPropertySet(self):

        localctx = ShExDocParser.InclPropertySetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_inclPropertySet)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(ShExDocParser.KW_EXTRA)
            self.state = 197 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 196
                self.predicate()
                self.state = 199 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ShExDocParser.RDF_TYPE) | (1 << ShExDocParser.IRIREF) | (1 << ShExDocParser.PNAME_NS) | (1 << ShExDocParser.PNAME_LN))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SomeOfShapeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def groupShape(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShExDocParser.GroupShapeContext)
            else:
                return self.getTypedRuleContext(ShExDocParser.GroupShapeContext,i)


        def getRuleIndex(self):
            return ShExDocParser.RULE_someOfShape

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitSomeOfShape(self)
            else:
                return visitor.visitChildren(self)




    def someOfShape(self):

        localctx = ShExDocParser.SomeOfShapeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_someOfShape)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.groupShape()
            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ShExDocParser.T__6:
                self.state = 202
                self.match(ShExDocParser.T__6)
                self.state = 203
                self.groupShape()
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GroupShapeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryShape(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShExDocParser.UnaryShapeContext)
            else:
                return self.getTypedRuleContext(ShExDocParser.UnaryShapeContext,i)


        def getRuleIndex(self):
            return ShExDocParser.RULE_groupShape

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitGroupShape(self)
            else:
                return visitor.visitChildren(self)




    def groupShape(self):

        localctx = ShExDocParser.GroupShapeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_groupShape)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.unaryShape()
            self.state = 214
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 210
                    self.match(ShExDocParser.T__7)
                    self.state = 211
                    self.unaryShape() 
                self.state = 216
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 218
            _la = self._input.LA(1)
            if _la==ShExDocParser.T__7:
                self.state = 217
                self.match(ShExDocParser.T__7)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UnaryShapeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tripleConstraint(self):
            return self.getTypedRuleContext(ShExDocParser.TripleConstraintContext,0)


        def include(self):
            return self.getTypedRuleContext(ShExDocParser.IncludeContext,0)


        def someOfShape(self):
            return self.getTypedRuleContext(ShExDocParser.SomeOfShapeContext,0)


        def semanticActions(self):
            return self.getTypedRuleContext(ShExDocParser.SemanticActionsContext,0)


        def cardinality(self):
            return self.getTypedRuleContext(ShExDocParser.CardinalityContext,0)


        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShExDocParser.AnnotationContext)
            else:
                return self.getTypedRuleContext(ShExDocParser.AnnotationContext,i)


        def getRuleIndex(self):
            return ShExDocParser.RULE_unaryShape

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitUnaryShape(self)
            else:
                return visitor.visitChildren(self)




    def unaryShape(self):

        localctx = ShExDocParser.UnaryShapeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_unaryShape)
        self._la = 0 # Token type
        try:
            self.state = 236
            token = self._input.LA(1)
            if token in [ShExDocParser.T__10, ShExDocParser.T__11, ShExDocParser.RDF_TYPE, ShExDocParser.IRIREF, ShExDocParser.PNAME_NS, ShExDocParser.PNAME_LN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.tripleConstraint()

            elif token in [ShExDocParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.include()

            elif token in [ShExDocParser.T__8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 222
                self.match(ShExDocParser.T__8)
                self.state = 223
                self.someOfShape()
                self.state = 224
                self.match(ShExDocParser.T__9)
                self.state = 226
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ShExDocParser.T__1) | (1 << ShExDocParser.T__3) | (1 << ShExDocParser.T__16) | (1 << ShExDocParser.T__17))) != 0):
                    self.state = 225
                    self.cardinality()


                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ShExDocParser.T__15:
                    self.state = 228
                    self.annotation()
                    self.state = 233
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 234
                self.semanticActions()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IncludeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def shapeLabel(self):
            return self.getTypedRuleContext(ShExDocParser.ShapeLabelContext,0)


        def getRuleIndex(self):
            return ShExDocParser.RULE_include

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitInclude(self)
            else:
                return visitor.visitChildren(self)




    def include(self):

        localctx = ShExDocParser.IncludeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_include)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(ShExDocParser.T__5)
            self.state = 239
            self.shapeLabel()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ShapeLabelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def iri(self):
            return self.getTypedRuleContext(ShExDocParser.IriContext,0)


        def blankNode(self):
            return self.getTypedRuleContext(ShExDocParser.BlankNodeContext,0)


        def getRuleIndex(self):
            return ShExDocParser.RULE_shapeLabel

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitShapeLabel(self)
            else:
                return visitor.visitChildren(self)




    def shapeLabel(self):

        localctx = ShExDocParser.ShapeLabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_shapeLabel)
        try:
            self.state = 243
            token = self._input.LA(1)
            if token in [ShExDocParser.IRIREF, ShExDocParser.PNAME_NS, ShExDocParser.PNAME_LN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.iri()

            elif token in [ShExDocParser.BLANK_NODE_LABEL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                self.blankNode()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TripleConstraintContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def predicate(self):
            return self.getTypedRuleContext(ShExDocParser.PredicateContext,0)


        def valueClassOrRef(self):
            return self.getTypedRuleContext(ShExDocParser.ValueClassOrRefContext,0)


        def semanticActions(self):
            return self.getTypedRuleContext(ShExDocParser.SemanticActionsContext,0)


        def senseFlags(self):
            return self.getTypedRuleContext(ShExDocParser.SenseFlagsContext,0)


        def cardinality(self):
            return self.getTypedRuleContext(ShExDocParser.CardinalityContext,0)


        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShExDocParser.AnnotationContext)
            else:
                return self.getTypedRuleContext(ShExDocParser.AnnotationContext,i)


        def getRuleIndex(self):
            return ShExDocParser.RULE_tripleConstraint

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitTripleConstraint(self)
            else:
                return visitor.visitChildren(self)




    def tripleConstraint(self):

        localctx = ShExDocParser.TripleConstraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_tripleConstraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            _la = self._input.LA(1)
            if _la==ShExDocParser.T__10 or _la==ShExDocParser.T__11:
                self.state = 245
                self.senseFlags()


            self.state = 248
            self.predicate()
            self.state = 249
            self.valueClassOrRef()
            self.state = 251
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ShExDocParser.T__1) | (1 << ShExDocParser.T__3) | (1 << ShExDocParser.T__16) | (1 << ShExDocParser.T__17))) != 0):
                self.state = 250
                self.cardinality()


            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ShExDocParser.T__15:
                self.state = 253
                self.annotation()
                self.state = 258
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 259
            self.semanticActions()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SenseFlagsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ShExDocParser.RULE_senseFlags

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitSenseFlags(self)
            else:
                return visitor.visitChildren(self)




    def senseFlags(self):

        localctx = ShExDocParser.SenseFlagsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_senseFlags)
        self._la = 0 # Token type
        try:
            self.state = 269
            token = self._input.LA(1)
            if token in [ShExDocParser.T__10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.match(ShExDocParser.T__10)
                self.state = 263
                _la = self._input.LA(1)
                if _la==ShExDocParser.T__11:
                    self.state = 262
                    self.match(ShExDocParser.T__11)



            elif token in [ShExDocParser.T__11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 265
                self.match(ShExDocParser.T__11)
                self.state = 267
                _la = self._input.LA(1)
                if _la==ShExDocParser.T__10:
                    self.state = 266
                    self.match(ShExDocParser.T__10)



            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PredicateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def iri(self):
            return self.getTypedRuleContext(ShExDocParser.IriContext,0)


        def RDF_TYPE(self):
            return self.getToken(ShExDocParser.RDF_TYPE, 0)

        def getRuleIndex(self):
            return ShExDocParser.RULE_predicate

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitPredicate(self)
            else:
                return visitor.visitChildren(self)




    def predicate(self):

        localctx = ShExDocParser.PredicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_predicate)
        try:
            self.state = 273
            token = self._input.LA(1)
            if token in [ShExDocParser.IRIREF, ShExDocParser.PNAME_NS, ShExDocParser.PNAME_LN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.iri()

            elif token in [ShExDocParser.RDF_TYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 272
                self.match(ShExDocParser.RDF_TYPE)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueClassOrRefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def valueClass(self):
            return self.getTypedRuleContext(ShExDocParser.ValueClassContext,0)


        def valueClassLabel(self):
            return self.getTypedRuleContext(ShExDocParser.ValueClassLabelContext,0)


        def getRuleIndex(self):
            return ShExDocParser.RULE_valueClassOrRef

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitValueClassOrRef(self)
            else:
                return visitor.visitChildren(self)




    def valueClassOrRef(self):

        localctx = ShExDocParser.ValueClassOrRefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_valueClassOrRef)
        try:
            self.state = 277
            token = self._input.LA(1)
            if token in [ShExDocParser.T__3, ShExDocParser.T__5, ShExDocParser.T__8, ShExDocParser.T__12, ShExDocParser.T__13, ShExDocParser.KW_CLOSED, ShExDocParser.KW_EXTRA, ShExDocParser.KW_LITERAL, ShExDocParser.KW_IRI, ShExDocParser.KW_NONLITERAL, ShExDocParser.KW_BNODE, ShExDocParser.IRIREF, ShExDocParser.PNAME_NS, ShExDocParser.PNAME_LN, ShExDocParser.ATPNAME_NS, ShExDocParser.ATPNAME_LN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.valueClass()

            elif token in [ShExDocParser.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.valueClassLabel()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueClassContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ShExDocParser.RULE_valueClass

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ValueClassValueSetContext(ValueClassContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShExDocParser.ValueClassContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def valueSet(self):
            return self.getTypedRuleContext(ShExDocParser.ValueSetContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitValueClassValueSet(self)
            else:
                return visitor.visitChildren(self)


    class ValueClassNonLiteralContext(ValueClassContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShExDocParser.ValueClassContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_IRI(self):
            return self.getToken(ShExDocParser.KW_IRI, 0)
        def KW_BNODE(self):
            return self.getToken(ShExDocParser.KW_BNODE, 0)
        def KW_NONLITERAL(self):
            return self.getToken(ShExDocParser.KW_NONLITERAL, 0)
        def groupShapeConstr(self):
            return self.getTypedRuleContext(ShExDocParser.GroupShapeConstrContext,0)

        def stringFacet(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShExDocParser.StringFacetContext)
            else:
                return self.getTypedRuleContext(ShExDocParser.StringFacetContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitValueClassNonLiteral(self)
            else:
                return visitor.visitChildren(self)


    class ValueClassDatatypeContext(ValueClassContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShExDocParser.ValueClassContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def datatype(self):
            return self.getTypedRuleContext(ShExDocParser.DatatypeContext,0)

        def xsFacet(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShExDocParser.XsFacetContext)
            else:
                return self.getTypedRuleContext(ShExDocParser.XsFacetContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitValueClassDatatype(self)
            else:
                return visitor.visitChildren(self)


    class ValueClassAnyContext(ValueClassContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShExDocParser.ValueClassContext)
            super().__init__(parser)
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitValueClassAny(self)
            else:
                return visitor.visitChildren(self)


    class ValueClassGroupContext(ValueClassContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShExDocParser.ValueClassContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def groupShapeConstr(self):
            return self.getTypedRuleContext(ShExDocParser.GroupShapeConstrContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitValueClassGroup(self)
            else:
                return visitor.visitChildren(self)


    class ValueClassLiteralContext(ValueClassContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShExDocParser.ValueClassContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_LITERAL(self):
            return self.getToken(ShExDocParser.KW_LITERAL, 0)
        def xsFacet(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShExDocParser.XsFacetContext)
            else:
                return self.getTypedRuleContext(ShExDocParser.XsFacetContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitValueClassLiteral(self)
            else:
                return visitor.visitChildren(self)



    def valueClass(self):

        localctx = ShExDocParser.ValueClassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_valueClass)
        self._la = 0 # Token type
        try:
            self.state = 306
            token = self._input.LA(1)
            if token in [ShExDocParser.KW_LITERAL]:
                localctx = ShExDocParser.ValueClassLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.match(ShExDocParser.KW_LITERAL)
                self.state = 283
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ShExDocParser.T__14) | (1 << ShExDocParser.KW_PATTERN) | (1 << ShExDocParser.KW_MININCLUSIVE) | (1 << ShExDocParser.KW_MINEXCLUSIVE) | (1 << ShExDocParser.KW_MAXINCLUSIVE) | (1 << ShExDocParser.KW_MAXEXCLUSIVE) | (1 << ShExDocParser.KW_LENGTH) | (1 << ShExDocParser.KW_MINLENGTH) | (1 << ShExDocParser.KW_MAXLENGTH) | (1 << ShExDocParser.KW_TOTALDIGITS) | (1 << ShExDocParser.KW_FRACTIONDIGITS))) != 0):
                    self.state = 280
                    self.xsFacet()
                    self.state = 285
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)


            elif token in [ShExDocParser.KW_IRI, ShExDocParser.KW_NONLITERAL, ShExDocParser.KW_BNODE]:
                localctx = ShExDocParser.ValueClassNonLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 286
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ShExDocParser.KW_IRI) | (1 << ShExDocParser.KW_NONLITERAL) | (1 << ShExDocParser.KW_BNODE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 288
                la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                if la_ == 1:
                    self.state = 287
                    self.groupShapeConstr()


                self.state = 293
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ShExDocParser.T__14) | (1 << ShExDocParser.KW_PATTERN) | (1 << ShExDocParser.KW_LENGTH) | (1 << ShExDocParser.KW_MINLENGTH) | (1 << ShExDocParser.KW_MAXLENGTH))) != 0):
                    self.state = 290
                    self.stringFacet()
                    self.state = 295
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)


            elif token in [ShExDocParser.IRIREF, ShExDocParser.PNAME_NS, ShExDocParser.PNAME_LN]:
                localctx = ShExDocParser.ValueClassDatatypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 296
                self.datatype()
                self.state = 300
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ShExDocParser.T__14) | (1 << ShExDocParser.KW_PATTERN) | (1 << ShExDocParser.KW_MININCLUSIVE) | (1 << ShExDocParser.KW_MINEXCLUSIVE) | (1 << ShExDocParser.KW_MAXINCLUSIVE) | (1 << ShExDocParser.KW_MAXEXCLUSIVE) | (1 << ShExDocParser.KW_LENGTH) | (1 << ShExDocParser.KW_MINLENGTH) | (1 << ShExDocParser.KW_MAXLENGTH) | (1 << ShExDocParser.KW_TOTALDIGITS) | (1 << ShExDocParser.KW_FRACTIONDIGITS))) != 0):
                    self.state = 297
                    self.xsFacet()
                    self.state = 302
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)


            elif token in [ShExDocParser.T__3, ShExDocParser.T__5, ShExDocParser.T__13, ShExDocParser.KW_CLOSED, ShExDocParser.KW_EXTRA, ShExDocParser.ATPNAME_NS, ShExDocParser.ATPNAME_LN]:
                localctx = ShExDocParser.ValueClassGroupContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 303
                self.groupShapeConstr()

            elif token in [ShExDocParser.T__8]:
                localctx = ShExDocParser.ValueClassValueSetContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 304
                self.valueSet()

            elif token in [ShExDocParser.T__12]:
                localctx = ShExDocParser.ValueClassAnyContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 305
                self.match(ShExDocParser.T__12)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GroupShapeConstrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def shapeOrRef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShExDocParser.ShapeOrRefContext)
            else:
                return self.getTypedRuleContext(ShExDocParser.ShapeOrRefContext,i)


        def KW_OR(self, i:int=None):
            if i is None:
                return self.getTokens(ShExDocParser.KW_OR)
            else:
                return self.getToken(ShExDocParser.KW_OR, i)

        def getRuleIndex(self):
            return ShExDocParser.RULE_groupShapeConstr

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitGroupShapeConstr(self)
            else:
                return visitor.visitChildren(self)




    def groupShapeConstr(self):

        localctx = ShExDocParser.GroupShapeConstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_groupShapeConstr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.shapeOrRef()
            self.state = 313
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ShExDocParser.KW_OR:
                self.state = 309
                self.match(ShExDocParser.KW_OR)
                self.state = 310
                self.shapeOrRef()
                self.state = 315
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ShapeOrRefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATPNAME_LN(self):
            return self.getToken(ShExDocParser.ATPNAME_LN, 0)

        def ATPNAME_NS(self):
            return self.getToken(ShExDocParser.ATPNAME_NS, 0)

        def shapeLabel(self):
            return self.getTypedRuleContext(ShExDocParser.ShapeLabelContext,0)


        def shapeDefinition(self):
            return self.getTypedRuleContext(ShExDocParser.ShapeDefinitionContext,0)


        def getRuleIndex(self):
            return ShExDocParser.RULE_shapeOrRef

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitShapeOrRef(self)
            else:
                return visitor.visitChildren(self)




    def shapeOrRef(self):

        localctx = ShExDocParser.ShapeOrRefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_shapeOrRef)
        try:
            self.state = 321
            token = self._input.LA(1)
            if token in [ShExDocParser.ATPNAME_LN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.match(ShExDocParser.ATPNAME_LN)

            elif token in [ShExDocParser.ATPNAME_NS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                self.match(ShExDocParser.ATPNAME_NS)

            elif token in [ShExDocParser.T__13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 318
                self.match(ShExDocParser.T__13)
                self.state = 319
                self.shapeLabel()

            elif token in [ShExDocParser.T__3, ShExDocParser.T__5, ShExDocParser.KW_CLOSED, ShExDocParser.KW_EXTRA]:
                self.enterOuterAlt(localctx, 4)
                self.state = 320
                self.shapeDefinition()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class XsFacetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stringFacet(self):
            return self.getTypedRuleContext(ShExDocParser.StringFacetContext,0)


        def numericFacet(self):
            return self.getTypedRuleContext(ShExDocParser.NumericFacetContext,0)


        def getRuleIndex(self):
            return ShExDocParser.RULE_xsFacet

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitXsFacet(self)
            else:
                return visitor.visitChildren(self)




    def xsFacet(self):

        localctx = ShExDocParser.XsFacetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_xsFacet)
        try:
            self.state = 325
            token = self._input.LA(1)
            if token in [ShExDocParser.T__14, ShExDocParser.KW_PATTERN, ShExDocParser.KW_LENGTH, ShExDocParser.KW_MINLENGTH, ShExDocParser.KW_MAXLENGTH]:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.stringFacet()

            elif token in [ShExDocParser.KW_MININCLUSIVE, ShExDocParser.KW_MINEXCLUSIVE, ShExDocParser.KW_MAXINCLUSIVE, ShExDocParser.KW_MAXEXCLUSIVE, ShExDocParser.KW_TOTALDIGITS, ShExDocParser.KW_FRACTIONDIGITS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                self.numericFacet()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StringFacetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stringLength(self):
            return self.getTypedRuleContext(ShExDocParser.StringLengthContext,0)


        def INTEGER(self):
            return self.getToken(ShExDocParser.INTEGER, 0)

        def KW_PATTERN(self):
            return self.getToken(ShExDocParser.KW_PATTERN, 0)

        def string(self):
            return self.getTypedRuleContext(ShExDocParser.StringContext,0)


        def getRuleIndex(self):
            return ShExDocParser.RULE_stringFacet

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitStringFacet(self)
            else:
                return visitor.visitChildren(self)




    def stringFacet(self):

        localctx = ShExDocParser.StringFacetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_stringFacet)
        try:
            self.state = 334
            token = self._input.LA(1)
            if token in [ShExDocParser.KW_LENGTH, ShExDocParser.KW_MINLENGTH, ShExDocParser.KW_MAXLENGTH]:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.stringLength()
                self.state = 328
                self.match(ShExDocParser.INTEGER)

            elif token in [ShExDocParser.KW_PATTERN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
                self.match(ShExDocParser.KW_PATTERN)
                self.state = 331
                self.string()

            elif token in [ShExDocParser.T__14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 332
                self.match(ShExDocParser.T__14)
                self.state = 333
                self.string()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StringLengthContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_LENGTH(self):
            return self.getToken(ShExDocParser.KW_LENGTH, 0)

        def KW_MINLENGTH(self):
            return self.getToken(ShExDocParser.KW_MINLENGTH, 0)

        def KW_MAXLENGTH(self):
            return self.getToken(ShExDocParser.KW_MAXLENGTH, 0)

        def getRuleIndex(self):
            return ShExDocParser.RULE_stringLength

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitStringLength(self)
            else:
                return visitor.visitChildren(self)




    def stringLength(self):

        localctx = ShExDocParser.StringLengthContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_stringLength)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ShExDocParser.KW_LENGTH) | (1 << ShExDocParser.KW_MINLENGTH) | (1 << ShExDocParser.KW_MAXLENGTH))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumericFacetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numericRange(self):
            return self.getTypedRuleContext(ShExDocParser.NumericRangeContext,0)


        def INTEGER(self):
            return self.getToken(ShExDocParser.INTEGER, 0)

        def numericLength(self):
            return self.getTypedRuleContext(ShExDocParser.NumericLengthContext,0)


        def getRuleIndex(self):
            return ShExDocParser.RULE_numericFacet

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitNumericFacet(self)
            else:
                return visitor.visitChildren(self)




    def numericFacet(self):

        localctx = ShExDocParser.NumericFacetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_numericFacet)
        try:
            self.state = 344
            token = self._input.LA(1)
            if token in [ShExDocParser.KW_MININCLUSIVE, ShExDocParser.KW_MINEXCLUSIVE, ShExDocParser.KW_MAXINCLUSIVE, ShExDocParser.KW_MAXEXCLUSIVE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.numericRange()
                self.state = 339
                self.match(ShExDocParser.INTEGER)

            elif token in [ShExDocParser.KW_TOTALDIGITS, ShExDocParser.KW_FRACTIONDIGITS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
                self.numericLength()
                self.state = 342
                self.match(ShExDocParser.INTEGER)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumericRangeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_MININCLUSIVE(self):
            return self.getToken(ShExDocParser.KW_MININCLUSIVE, 0)

        def KW_MINEXCLUSIVE(self):
            return self.getToken(ShExDocParser.KW_MINEXCLUSIVE, 0)

        def KW_MAXINCLUSIVE(self):
            return self.getToken(ShExDocParser.KW_MAXINCLUSIVE, 0)

        def KW_MAXEXCLUSIVE(self):
            return self.getToken(ShExDocParser.KW_MAXEXCLUSIVE, 0)

        def getRuleIndex(self):
            return ShExDocParser.RULE_numericRange

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitNumericRange(self)
            else:
                return visitor.visitChildren(self)




    def numericRange(self):

        localctx = ShExDocParser.NumericRangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_numericRange)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ShExDocParser.KW_MININCLUSIVE) | (1 << ShExDocParser.KW_MINEXCLUSIVE) | (1 << ShExDocParser.KW_MAXINCLUSIVE) | (1 << ShExDocParser.KW_MAXEXCLUSIVE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumericLengthContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_TOTALDIGITS(self):
            return self.getToken(ShExDocParser.KW_TOTALDIGITS, 0)

        def KW_FRACTIONDIGITS(self):
            return self.getToken(ShExDocParser.KW_FRACTIONDIGITS, 0)

        def getRuleIndex(self):
            return ShExDocParser.RULE_numericLength

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitNumericLength(self)
            else:
                return visitor.visitChildren(self)




    def numericLength(self):

        localctx = ShExDocParser.NumericLengthContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_numericLength)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            _la = self._input.LA(1)
            if not(_la==ShExDocParser.KW_TOTALDIGITS or _la==ShExDocParser.KW_FRACTIONDIGITS):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DatatypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def iri(self):
            return self.getTypedRuleContext(ShExDocParser.IriContext,0)


        def getRuleIndex(self):
            return ShExDocParser.RULE_datatype

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitDatatype(self)
            else:
                return visitor.visitChildren(self)




    def datatype(self):

        localctx = ShExDocParser.DatatypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_datatype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.iri()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AnnotationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def iri(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShExDocParser.IriContext)
            else:
                return self.getTypedRuleContext(ShExDocParser.IriContext,i)


        def literal(self):
            return self.getTypedRuleContext(ShExDocParser.LiteralContext,0)


        def getRuleIndex(self):
            return ShExDocParser.RULE_annotation

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitAnnotation(self)
            else:
                return visitor.visitChildren(self)




    def annotation(self):

        localctx = ShExDocParser.AnnotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_annotation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.match(ShExDocParser.T__15)
            self.state = 353
            self.iri()
            self.state = 356
            token = self._input.LA(1)
            if token in [ShExDocParser.IRIREF, ShExDocParser.PNAME_NS, ShExDocParser.PNAME_LN]:
                self.state = 354
                self.iri()

            elif token in [ShExDocParser.KW_TRUE, ShExDocParser.KW_FALSE, ShExDocParser.INTEGER, ShExDocParser.DECIMAL, ShExDocParser.DOUBLE, ShExDocParser.STRING_LITERAL1, ShExDocParser.STRING_LITERAL2, ShExDocParser.STRING_LITERAL_LONG1, ShExDocParser.STRING_LITERAL_LONG2]:
                self.state = 355
                self.literal()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CardinalityContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def repeatRange(self):
            return self.getTypedRuleContext(ShExDocParser.RepeatRangeContext,0)


        def getRuleIndex(self):
            return ShExDocParser.RULE_cardinality

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitCardinality(self)
            else:
                return visitor.visitChildren(self)




    def cardinality(self):

        localctx = ShExDocParser.CardinalityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_cardinality)
        try:
            self.state = 362
            token = self._input.LA(1)
            if token in [ShExDocParser.T__16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.match(ShExDocParser.T__16)

            elif token in [ShExDocParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
                self.match(ShExDocParser.T__1)

            elif token in [ShExDocParser.T__17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 360
                self.match(ShExDocParser.T__17)

            elif token in [ShExDocParser.T__3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 361
                self.repeatRange()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RepeatRangeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self, i:int=None):
            if i is None:
                return self.getTokens(ShExDocParser.INTEGER)
            else:
                return self.getToken(ShExDocParser.INTEGER, i)

        def getRuleIndex(self):
            return ShExDocParser.RULE_repeatRange

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitRepeatRange(self)
            else:
                return visitor.visitChildren(self)




    def repeatRange(self):

        localctx = ShExDocParser.RepeatRangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_repeatRange)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.match(ShExDocParser.T__3)
            self.state = 365
            self.match(ShExDocParser.INTEGER)
            self.state = 370
            _la = self._input.LA(1)
            if _la==ShExDocParser.T__7:
                self.state = 366
                self.match(ShExDocParser.T__7)
                self.state = 368
                _la = self._input.LA(1)
                if _la==ShExDocParser.T__16 or _la==ShExDocParser.INTEGER:
                    self.state = 367
                    _la = self._input.LA(1)
                    if not(_la==ShExDocParser.T__16 or _la==ShExDocParser.INTEGER):
                        self._errHandler.recoverInline(self)
                    else:
                        self.consume()




            self.state = 372
            self.match(ShExDocParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueSetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShExDocParser.ValueContext)
            else:
                return self.getTypedRuleContext(ShExDocParser.ValueContext,i)


        def getRuleIndex(self):
            return ShExDocParser.RULE_valueSet

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitValueSet(self)
            else:
                return visitor.visitChildren(self)




    def valueSet(self):

        localctx = ShExDocParser.ValueSetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_valueSet)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(ShExDocParser.T__8)
            self.state = 378
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 13)) & ~0x3f) == 0 and ((1 << (_la - 13)) & ((1 << (ShExDocParser.T__12 - 13)) | (1 << (ShExDocParser.KW_TRUE - 13)) | (1 << (ShExDocParser.KW_FALSE - 13)) | (1 << (ShExDocParser.IRIREF - 13)) | (1 << (ShExDocParser.PNAME_NS - 13)) | (1 << (ShExDocParser.PNAME_LN - 13)) | (1 << (ShExDocParser.INTEGER - 13)) | (1 << (ShExDocParser.DECIMAL - 13)) | (1 << (ShExDocParser.DOUBLE - 13)) | (1 << (ShExDocParser.STRING_LITERAL1 - 13)) | (1 << (ShExDocParser.STRING_LITERAL2 - 13)) | (1 << (ShExDocParser.STRING_LITERAL_LONG1 - 13)) | (1 << (ShExDocParser.STRING_LITERAL_LONG2 - 13)))) != 0):
                self.state = 375
                self.value()
                self.state = 380
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 381
            self.match(ShExDocParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def iriRange(self):
            return self.getTypedRuleContext(ShExDocParser.IriRangeContext,0)


        def literal(self):
            return self.getTypedRuleContext(ShExDocParser.LiteralContext,0)


        def getRuleIndex(self):
            return ShExDocParser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = ShExDocParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_value)
        try:
            self.state = 385
            token = self._input.LA(1)
            if token in [ShExDocParser.T__12, ShExDocParser.IRIREF, ShExDocParser.PNAME_NS, ShExDocParser.PNAME_LN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 383
                self.iriRange()

            elif token in [ShExDocParser.KW_TRUE, ShExDocParser.KW_FALSE, ShExDocParser.INTEGER, ShExDocParser.DECIMAL, ShExDocParser.DOUBLE, ShExDocParser.STRING_LITERAL1, ShExDocParser.STRING_LITERAL2, ShExDocParser.STRING_LITERAL_LONG1, ShExDocParser.STRING_LITERAL_LONG2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 384
                self.literal()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IriRangeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def iri(self):
            return self.getTypedRuleContext(ShExDocParser.IriContext,0)


        def exclusion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShExDocParser.ExclusionContext)
            else:
                return self.getTypedRuleContext(ShExDocParser.ExclusionContext,i)


        def getRuleIndex(self):
            return ShExDocParser.RULE_iriRange

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitIriRange(self)
            else:
                return visitor.visitChildren(self)




    def iriRange(self):

        localctx = ShExDocParser.IriRangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_iriRange)
        self._la = 0 # Token type
        try:
            self.state = 403
            token = self._input.LA(1)
            if token in [ShExDocParser.IRIREF, ShExDocParser.PNAME_NS, ShExDocParser.PNAME_LN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.iri()
                self.state = 395
                _la = self._input.LA(1)
                if _la==ShExDocParser.T__14:
                    self.state = 388
                    self.match(ShExDocParser.T__14)
                    self.state = 392
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==ShExDocParser.T__18:
                        self.state = 389
                        self.exclusion()
                        self.state = 394
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)




            elif token in [ShExDocParser.T__12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 397
                self.match(ShExDocParser.T__12)
                self.state = 399 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 398
                    self.exclusion()
                    self.state = 401 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ShExDocParser.T__18):
                        break


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExclusionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def iri(self):
            return self.getTypedRuleContext(ShExDocParser.IriContext,0)


        def getRuleIndex(self):
            return ShExDocParser.RULE_exclusion

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitExclusion(self)
            else:
                return visitor.visitChildren(self)




    def exclusion(self):

        localctx = ShExDocParser.ExclusionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_exclusion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.match(ShExDocParser.T__18)
            self.state = 406
            self.iri()
            self.state = 408
            _la = self._input.LA(1)
            if _la==ShExDocParser.T__14:
                self.state = 407
                self.match(ShExDocParser.T__14)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rdfLiteral(self):
            return self.getTypedRuleContext(ShExDocParser.RdfLiteralContext,0)


        def numericLiteral(self):
            return self.getTypedRuleContext(ShExDocParser.NumericLiteralContext,0)


        def booleanLiteral(self):
            return self.getTypedRuleContext(ShExDocParser.BooleanLiteralContext,0)


        def getRuleIndex(self):
            return ShExDocParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ShExDocParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_literal)
        try:
            self.state = 413
            token = self._input.LA(1)
            if token in [ShExDocParser.STRING_LITERAL1, ShExDocParser.STRING_LITERAL2, ShExDocParser.STRING_LITERAL_LONG1, ShExDocParser.STRING_LITERAL_LONG2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 410
                self.rdfLiteral()

            elif token in [ShExDocParser.INTEGER, ShExDocParser.DECIMAL, ShExDocParser.DOUBLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 411
                self.numericLiteral()

            elif token in [ShExDocParser.KW_TRUE, ShExDocParser.KW_FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 412
                self.booleanLiteral()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumericLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(ShExDocParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(ShExDocParser.DECIMAL, 0)

        def DOUBLE(self):
            return self.getToken(ShExDocParser.DOUBLE, 0)

        def getRuleIndex(self):
            return ShExDocParser.RULE_numericLiteral

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitNumericLiteral(self)
            else:
                return visitor.visitChildren(self)




    def numericLiteral(self):

        localctx = ShExDocParser.NumericLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_numericLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ShExDocParser.INTEGER) | (1 << ShExDocParser.DECIMAL) | (1 << ShExDocParser.DOUBLE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RdfLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(ShExDocParser.StringContext,0)


        def LANGTAG(self):
            return self.getToken(ShExDocParser.LANGTAG, 0)

        def datatype(self):
            return self.getTypedRuleContext(ShExDocParser.DatatypeContext,0)


        def getRuleIndex(self):
            return ShExDocParser.RULE_rdfLiteral

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitRdfLiteral(self)
            else:
                return visitor.visitChildren(self)




    def rdfLiteral(self):

        localctx = ShExDocParser.RdfLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_rdfLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.string()
            self.state = 421
            token = self._input.LA(1)
            if token in [ShExDocParser.LANGTAG]:
                self.state = 418
                self.match(ShExDocParser.LANGTAG)
                pass
            elif token in [ShExDocParser.T__19]:
                self.state = 419
                self.match(ShExDocParser.T__19)
                self.state = 420
                self.datatype()
                pass
            elif token in [ShExDocParser.T__4, ShExDocParser.T__6, ShExDocParser.T__7, ShExDocParser.T__9, ShExDocParser.T__12, ShExDocParser.T__15, ShExDocParser.T__20, ShExDocParser.KW_TRUE, ShExDocParser.KW_FALSE, ShExDocParser.IRIREF, ShExDocParser.PNAME_NS, ShExDocParser.PNAME_LN, ShExDocParser.INTEGER, ShExDocParser.DECIMAL, ShExDocParser.DOUBLE, ShExDocParser.STRING_LITERAL1, ShExDocParser.STRING_LITERAL2, ShExDocParser.STRING_LITERAL_LONG1, ShExDocParser.STRING_LITERAL_LONG2]:
                pass
            else:
                raise NoViableAltException(self)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BooleanLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_TRUE(self):
            return self.getToken(ShExDocParser.KW_TRUE, 0)

        def KW_FALSE(self):
            return self.getToken(ShExDocParser.KW_FALSE, 0)

        def getRuleIndex(self):
            return ShExDocParser.RULE_booleanLiteral

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitBooleanLiteral(self)
            else:
                return visitor.visitChildren(self)




    def booleanLiteral(self):

        localctx = ShExDocParser.BooleanLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_booleanLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            _la = self._input.LA(1)
            if not(_la==ShExDocParser.KW_TRUE or _la==ShExDocParser.KW_FALSE):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StringContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LITERAL1(self):
            return self.getToken(ShExDocParser.STRING_LITERAL1, 0)

        def STRING_LITERAL2(self):
            return self.getToken(ShExDocParser.STRING_LITERAL2, 0)

        def STRING_LITERAL_LONG1(self):
            return self.getToken(ShExDocParser.STRING_LITERAL_LONG1, 0)

        def STRING_LITERAL_LONG2(self):
            return self.getToken(ShExDocParser.STRING_LITERAL_LONG2, 0)

        def getRuleIndex(self):
            return ShExDocParser.RULE_string

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = ShExDocParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            _la = self._input.LA(1)
            if not(((((_la - 62)) & ~0x3f) == 0 and ((1 << (_la - 62)) & ((1 << (ShExDocParser.STRING_LITERAL1 - 62)) | (1 << (ShExDocParser.STRING_LITERAL2 - 62)) | (1 << (ShExDocParser.STRING_LITERAL_LONG1 - 62)) | (1 << (ShExDocParser.STRING_LITERAL_LONG2 - 62)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IriContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IRIREF(self):
            return self.getToken(ShExDocParser.IRIREF, 0)

        def prefixedName(self):
            return self.getTypedRuleContext(ShExDocParser.PrefixedNameContext,0)


        def getRuleIndex(self):
            return ShExDocParser.RULE_iri

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitIri(self)
            else:
                return visitor.visitChildren(self)




    def iri(self):

        localctx = ShExDocParser.IriContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_iri)
        try:
            self.state = 429
            token = self._input.LA(1)
            if token in [ShExDocParser.IRIREF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 427
                self.match(ShExDocParser.IRIREF)

            elif token in [ShExDocParser.PNAME_NS, ShExDocParser.PNAME_LN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 428
                self.prefixedName()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrefixedNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PNAME_LN(self):
            return self.getToken(ShExDocParser.PNAME_LN, 0)

        def PNAME_NS(self):
            return self.getToken(ShExDocParser.PNAME_NS, 0)

        def getRuleIndex(self):
            return ShExDocParser.RULE_prefixedName

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitPrefixedName(self)
            else:
                return visitor.visitChildren(self)




    def prefixedName(self):

        localctx = ShExDocParser.PrefixedNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_prefixedName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            _la = self._input.LA(1)
            if not(_la==ShExDocParser.PNAME_NS or _la==ShExDocParser.PNAME_LN):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlankNodeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BLANK_NODE_LABEL(self):
            return self.getToken(ShExDocParser.BLANK_NODE_LABEL, 0)

        def getRuleIndex(self):
            return ShExDocParser.RULE_blankNode

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitBlankNode(self)
            else:
                return visitor.visitChildren(self)




    def blankNode(self):

        localctx = ShExDocParser.BlankNodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_blankNode)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self.match(ShExDocParser.BLANK_NODE_LABEL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CodeDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def codeLabel(self):
            return self.getTypedRuleContext(ShExDocParser.CodeLabelContext,0)


        def iri(self):
            return self.getTypedRuleContext(ShExDocParser.IriContext,0)


        def CODE(self):
            return self.getToken(ShExDocParser.CODE, 0)

        def getRuleIndex(self):
            return ShExDocParser.RULE_codeDecl

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitCodeDecl(self)
            else:
                return visitor.visitChildren(self)




    def codeDecl(self):

        localctx = ShExDocParser.CodeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_codeDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.match(ShExDocParser.T__20)
            self.state = 443
            token = self._input.LA(1)
            if token in [ShExDocParser.UCASE_LABEL]:
                self.state = 436
                self.codeLabel()

            elif token in [ShExDocParser.EOF, ShExDocParser.T__2, ShExDocParser.T__4, ShExDocParser.T__6, ShExDocParser.T__7, ShExDocParser.T__9, ShExDocParser.T__20, ShExDocParser.KW_BASE, ShExDocParser.KW_PREFIX, ShExDocParser.KW_START, ShExDocParser.KW_VIRTUAL, ShExDocParser.CODE, ShExDocParser.IRIREF, ShExDocParser.PNAME_NS, ShExDocParser.PNAME_LN, ShExDocParser.BLANK_NODE_LABEL]:
                self.state = 438
                la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
                if la_ == 1:
                    self.state = 437
                    self.iri()


                self.state = 441
                _la = self._input.LA(1)
                if _la==ShExDocParser.CODE:
                    self.state = 440
                    self.match(ShExDocParser.CODE)



            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CodeLabelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UCASE_LABEL(self):
            return self.getToken(ShExDocParser.UCASE_LABEL, 0)

        def getRuleIndex(self):
            return ShExDocParser.RULE_codeLabel

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitCodeLabel(self)
            else:
                return visitor.visitChildren(self)




    def codeLabel(self):

        localctx = ShExDocParser.CodeLabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_codeLabel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.match(ShExDocParser.UCASE_LABEL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StartActionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def codeDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShExDocParser.CodeDeclContext)
            else:
                return self.getTypedRuleContext(ShExDocParser.CodeDeclContext,i)


        def getRuleIndex(self):
            return ShExDocParser.RULE_startActions

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitStartActions(self)
            else:
                return visitor.visitChildren(self)




    def startActions(self):

        localctx = ShExDocParser.StartActionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_startActions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 447
                self.codeDecl()
                self.state = 450 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ShExDocParser.T__20):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SemanticActionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def codeDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShExDocParser.CodeDeclContext)
            else:
                return self.getTypedRuleContext(ShExDocParser.CodeDeclContext,i)


        def getRuleIndex(self):
            return ShExDocParser.RULE_semanticActions

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ShExDocVisitor ):
                return visitor.visitSemanticActions(self)
            else:
                return visitor.visitChildren(self)




    def semanticActions(self):

        localctx = ShExDocParser.SemanticActionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_semanticActions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ShExDocParser.T__20:
                self.state = 452
                self.codeDecl()
                self.state = 457
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




