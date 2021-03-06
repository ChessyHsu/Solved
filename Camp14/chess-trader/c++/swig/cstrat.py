# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.4
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_cstrat', [dirname(__file__)])
        except ImportError:
            import _cstrat
            return _cstrat
        if fp is not None:
            try:
                _mod = imp.load_module('_cstrat', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _cstrat = swig_import_helper()
    del swig_import_helper
else:
    import _cstrat
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _cstrat.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _cstrat.SwigPyIterator_value(self)
    def incr(self, n = 1): return _cstrat.SwigPyIterator_incr(self, n)
    def decr(self, n = 1): return _cstrat.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _cstrat.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _cstrat.SwigPyIterator_equal(self, *args)
    def copy(self): return _cstrat.SwigPyIterator_copy(self)
    def next(self): return _cstrat.SwigPyIterator_next(self)
    def __next__(self): return _cstrat.SwigPyIterator___next__(self)
    def previous(self): return _cstrat.SwigPyIterator_previous(self)
    def advance(self, *args): return _cstrat.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _cstrat.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _cstrat.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _cstrat.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _cstrat.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _cstrat.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _cstrat.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _cstrat.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class vector_s(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vector_s, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vector_s, name)
    __repr__ = _swig_repr
    def iterator(self): return _cstrat.vector_s_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _cstrat.vector_s___nonzero__(self)
    def __bool__(self): return _cstrat.vector_s___bool__(self)
    def __len__(self): return _cstrat.vector_s___len__(self)
    def pop(self): return _cstrat.vector_s_pop(self)
    def __getslice__(self, *args): return _cstrat.vector_s___getslice__(self, *args)
    def __setslice__(self, *args): return _cstrat.vector_s___setslice__(self, *args)
    def __delslice__(self, *args): return _cstrat.vector_s___delslice__(self, *args)
    def __delitem__(self, *args): return _cstrat.vector_s___delitem__(self, *args)
    def __getitem__(self, *args): return _cstrat.vector_s___getitem__(self, *args)
    def __setitem__(self, *args): return _cstrat.vector_s___setitem__(self, *args)
    def append(self, *args): return _cstrat.vector_s_append(self, *args)
    def empty(self): return _cstrat.vector_s_empty(self)
    def size(self): return _cstrat.vector_s_size(self)
    def clear(self): return _cstrat.vector_s_clear(self)
    def swap(self, *args): return _cstrat.vector_s_swap(self, *args)
    def get_allocator(self): return _cstrat.vector_s_get_allocator(self)
    def begin(self): return _cstrat.vector_s_begin(self)
    def end(self): return _cstrat.vector_s_end(self)
    def rbegin(self): return _cstrat.vector_s_rbegin(self)
    def rend(self): return _cstrat.vector_s_rend(self)
    def pop_back(self): return _cstrat.vector_s_pop_back(self)
    def erase(self, *args): return _cstrat.vector_s_erase(self, *args)
    def __init__(self, *args): 
        this = _cstrat.new_vector_s(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _cstrat.vector_s_push_back(self, *args)
    def front(self): return _cstrat.vector_s_front(self)
    def back(self): return _cstrat.vector_s_back(self)
    def assign(self, *args): return _cstrat.vector_s_assign(self, *args)
    def resize(self, *args): return _cstrat.vector_s_resize(self, *args)
    def insert(self, *args): return _cstrat.vector_s_insert(self, *args)
    def reserve(self, *args): return _cstrat.vector_s_reserve(self, *args)
    def capacity(self): return _cstrat.vector_s_capacity(self)
    __swig_destroy__ = _cstrat.delete_vector_s
    __del__ = lambda self : None;
vector_s_swigregister = _cstrat.vector_s_swigregister
vector_s_swigregister(vector_s)

class vector_o(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vector_o, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vector_o, name)
    __repr__ = _swig_repr
    def iterator(self): return _cstrat.vector_o_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _cstrat.vector_o___nonzero__(self)
    def __bool__(self): return _cstrat.vector_o___bool__(self)
    def __len__(self): return _cstrat.vector_o___len__(self)
    def pop(self): return _cstrat.vector_o_pop(self)
    def __getslice__(self, *args): return _cstrat.vector_o___getslice__(self, *args)
    def __setslice__(self, *args): return _cstrat.vector_o___setslice__(self, *args)
    def __delslice__(self, *args): return _cstrat.vector_o___delslice__(self, *args)
    def __delitem__(self, *args): return _cstrat.vector_o___delitem__(self, *args)
    def __getitem__(self, *args): return _cstrat.vector_o___getitem__(self, *args)
    def __setitem__(self, *args): return _cstrat.vector_o___setitem__(self, *args)
    def append(self, *args): return _cstrat.vector_o_append(self, *args)
    def empty(self): return _cstrat.vector_o_empty(self)
    def size(self): return _cstrat.vector_o_size(self)
    def clear(self): return _cstrat.vector_o_clear(self)
    def swap(self, *args): return _cstrat.vector_o_swap(self, *args)
    def get_allocator(self): return _cstrat.vector_o_get_allocator(self)
    def begin(self): return _cstrat.vector_o_begin(self)
    def end(self): return _cstrat.vector_o_end(self)
    def rbegin(self): return _cstrat.vector_o_rbegin(self)
    def rend(self): return _cstrat.vector_o_rend(self)
    def pop_back(self): return _cstrat.vector_o_pop_back(self)
    def erase(self, *args): return _cstrat.vector_o_erase(self, *args)
    def __init__(self, *args): 
        this = _cstrat.new_vector_o(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _cstrat.vector_o_push_back(self, *args)
    def front(self): return _cstrat.vector_o_front(self)
    def back(self): return _cstrat.vector_o_back(self)
    def assign(self, *args): return _cstrat.vector_o_assign(self, *args)
    def resize(self, *args): return _cstrat.vector_o_resize(self, *args)
    def insert(self, *args): return _cstrat.vector_o_insert(self, *args)
    def reserve(self, *args): return _cstrat.vector_o_reserve(self, *args)
    def capacity(self): return _cstrat.vector_o_capacity(self)
    __swig_destroy__ = _cstrat.delete_vector_o
    __del__ = lambda self : None;
vector_o_swigregister = _cstrat.vector_o_swigregister
vector_o_swigregister(vector_o)

class CBook(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CBook, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CBook, name)
    __repr__ = _swig_repr
    def bidLevels(self): return _cstrat.CBook_bidLevels(self)
    def askLevels(self): return _cstrat.CBook_askLevels(self)
    def bidPrice(self, *args): return _cstrat.CBook_bidPrice(self, *args)
    def askPrice(self, *args): return _cstrat.CBook_askPrice(self, *args)
    def bidQuantity(self, *args): return _cstrat.CBook_bidQuantity(self, *args)
    def askQuantity(self, *args): return _cstrat.CBook_askQuantity(self, *args)
    def bidOrders(self, *args): return _cstrat.CBook_bidOrders(self, *args)
    def askOrders(self, *args): return _cstrat.CBook_askOrders(self, *args)
    MAX_LEVELS = _cstrat.CBook_MAX_LEVELS
    def __init__(self): 
        this = _cstrat.new_CBook()
        try: self.this.append(this)
        except: self.this = this
    def reset(self): return _cstrat.CBook_reset(self)
    def setBid(self, *args): return _cstrat.CBook_setBid(self, *args)
    def setAsk(self, *args): return _cstrat.CBook_setAsk(self, *args)
    __swig_destroy__ = _cstrat.delete_CBook
    __del__ = lambda self : None;
CBook_swigregister = _cstrat.CBook_swigregister
CBook_swigregister(CBook)

class COrder(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, COrder, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, COrder, name)
    __repr__ = _swig_repr
    def gameid(self): return _cstrat.COrder_gameid(self)
    def orderid(self): return _cstrat.COrder_orderid(self)
    def price(self): return _cstrat.COrder_price(self)
    def quantity(self): return _cstrat.COrder_quantity(self)
    def side(self): return _cstrat.COrder_side(self)
    BUY = _cstrat.COrder_BUY
    SELL = _cstrat.COrder_SELL
    def __init__(self, *args): 
        this = _cstrat.new_COrder(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cstrat.delete_COrder
    __del__ = lambda self : None;
COrder_swigregister = _cstrat.COrder_swigregister
COrder_swigregister(COrder)

class CGateway(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CGateway, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CGateway, name)
    __repr__ = _swig_repr
    def position(self): return _cstrat.CGateway_position(self)
    def ordersPending(self): return _cstrat.CGateway_ordersPending(self)
    def ordersLive(self): return _cstrat.CGateway_ordersLive(self)
    def ordersCanceling(self): return _cstrat.CGateway_ordersCanceling(self)
    def addOrder(self, *args): return _cstrat.CGateway_addOrder(self, *args)
    def cancelOrder(self, *args): return _cstrat.CGateway_cancelOrder(self, *args)
    def __init__(self): 
        this = _cstrat.new_CGateway()
        try: self.this.append(this)
        except: self.this = this
    def reset(self): return _cstrat.CGateway_reset(self)
    def setPosition(self, *args): return _cstrat.CGateway_setPosition(self, *args)
    def setOrdersPending(self, *args): return _cstrat.CGateway_setOrdersPending(self, *args)
    def setOrdersLive(self, *args): return _cstrat.CGateway_setOrdersLive(self, *args)
    def setOrdersCanceling(self, *args): return _cstrat.CGateway_setOrdersCanceling(self, *args)
    def outboundAdds(self): return _cstrat.CGateway_outboundAdds(self)
    def outboundCancels(self): return _cstrat.CGateway_outboundCancels(self)
    __swig_destroy__ = _cstrat.delete_CGateway
    __del__ = lambda self : None;
CGateway_swigregister = _cstrat.CGateway_swigregister
CGateway_swigregister(CGateway)

CHESS_BOARD_DIM = _cstrat.CHESS_BOARD_DIM
class CBoard(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CBoard, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CBoard, name)
    __repr__ = _swig_repr
    def getPiece(self, *args): return _cstrat.CBoard_getPiece(self, *args)
    def __init__(self): 
        this = _cstrat.new_CBoard()
        try: self.this.append(this)
        except: self.this = this
    def setPiece(self, *args): return _cstrat.CBoard_setPiece(self, *args)
    __swig_destroy__ = _cstrat.delete_CBoard
    __del__ = lambda self : None;
CBoard_swigregister = _cstrat.CBoard_swigregister
CBoard_swigregister(CBoard)

class CStockfish(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CStockfish, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CStockfish, name)
    __repr__ = _swig_repr
    MATERIAL_PST_TEMPO = _cstrat.CStockfish_MATERIAL_PST_TEMPO
    MATERIAL_IMBALANCE = _cstrat.CStockfish_MATERIAL_IMBALANCE
    PAWNS = _cstrat.CStockfish_PAWNS
    KNIGHTS = _cstrat.CStockfish_KNIGHTS
    BISHOPS = _cstrat.CStockfish_BISHOPS
    ROOKS = _cstrat.CStockfish_ROOKS
    QUEENS = _cstrat.CStockfish_QUEENS
    MOBILITY = _cstrat.CStockfish_MOBILITY
    KING_SAFETY = _cstrat.CStockfish_KING_SAFETY
    THREATS = _cstrat.CStockfish_THREATS
    PASSED_PAWNS = _cstrat.CStockfish_PASSED_PAWNS
    SPACE = _cstrat.CStockfish_SPACE
    TOTAL = _cstrat.CStockfish_TOTAL
    NUM_SCORE_TYPES = _cstrat.CStockfish_NUM_SCORE_TYPES
    WHITE_MID_GAME = _cstrat.CStockfish_WHITE_MID_GAME
    WHITE_END_GAME = _cstrat.CStockfish_WHITE_END_GAME
    BLACK_MID_GAME = _cstrat.CStockfish_BLACK_MID_GAME
    BLACK_END_GAME = _cstrat.CStockfish_BLACK_END_GAME
    TOTAL_MID_GAME = _cstrat.CStockfish_TOTAL_MID_GAME
    TOTAL_END_GAME = _cstrat.CStockfish_TOTAL_END_GAME
    NUM_SCORE_SUBTYPES = _cstrat.CStockfish_NUM_SCORE_SUBTYPES
    def getFEN(self): return _cstrat.CStockfish_getFEN(self)
    def legalMoves(self): return _cstrat.CStockfish_legalMoves(self)
    def percentMidGame(self): return _cstrat.CStockfish_percentMidGame(self)
    def percentEndGame1(self): return _cstrat.CStockfish_percentEndGame1(self)
    def percentEndGame2(self): return _cstrat.CStockfish_percentEndGame2(self)
    def totalScore(self): return _cstrat.CStockfish_totalScore(self)
    def score(self, *args): return _cstrat.CStockfish_score(self, *args)
    def __init__(self): 
        this = _cstrat.new_CStockfish()
        try: self.this.append(this)
        except: self.this = this
    def reset(self): return _cstrat.CStockfish_reset(self)
    def setFEN(self, *args): return _cstrat.CStockfish_setFEN(self, *args)
    def setLegalMoves(self, *args): return _cstrat.CStockfish_setLegalMoves(self, *args)
    def setTotal(self, *args): return _cstrat.CStockfish_setTotal(self, *args)
    def setScore(self, *args): return _cstrat.CStockfish_setScore(self, *args)
    __swig_destroy__ = _cstrat.delete_CStockfish
    __del__ = lambda self : None;
CStockfish_swigregister = _cstrat.CStockfish_swigregister
CStockfish_swigregister(CStockfish)

class CExchangeMessage(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CExchangeMessage, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CExchangeMessage, name)
    __repr__ = _swig_repr
    EXCHANGE_UNKNOWN = _cstrat.CExchangeMessage_EXCHANGE_UNKNOWN
    EXCHANGE_NEW_GAME = _cstrat.CExchangeMessage_EXCHANGE_NEW_GAME
    EXCHANGE_ADD_ORDER = _cstrat.CExchangeMessage_EXCHANGE_ADD_ORDER
    EXCHANGE_CANCEL_ORDER = _cstrat.CExchangeMessage_EXCHANGE_CANCEL_ORDER
    EXCHANGE_TRADE = _cstrat.CExchangeMessage_EXCHANGE_TRADE
    def type(self): return _cstrat.CExchangeMessage_type(self)
    def order(self): return _cstrat.CExchangeMessage_order(self)
    def __init__(self, *args): 
        this = _cstrat.new_CExchangeMessage(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cstrat.delete_CExchangeMessage
    __del__ = lambda self : None;
CExchangeMessage_swigregister = _cstrat.CExchangeMessage_swigregister
CExchangeMessage_swigregister(CExchangeMessage)

class CChessMessage(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CChessMessage, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CChessMessage, name)
    __repr__ = _swig_repr
    CHESS_UNKNOWN = _cstrat.CChessMessage_CHESS_UNKNOWN
    CHESS_NEW_GAME = _cstrat.CChessMessage_CHESS_NEW_GAME
    CHESS_MOVE = _cstrat.CChessMessage_CHESS_MOVE
    CHESS_RESULT = _cstrat.CChessMessage_CHESS_RESULT
    def type(self): return _cstrat.CChessMessage_type(self)
    def gameid(self): return _cstrat.CChessMessage_gameid(self)
    def move(self): return _cstrat.CChessMessage_move(self)
    def history(self): return _cstrat.CChessMessage_history(self)
    def __init__(self, *args): 
        this = _cstrat.new_CChessMessage(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cstrat.delete_CChessMessage
    __del__ = lambda self : None;
CChessMessage_swigregister = _cstrat.CChessMessage_swigregister
CChessMessage_swigregister(CChessMessage)

class CStrategy(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CStrategy, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CStrategy, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    def onExchangeMessage(self, *args): return _cstrat.CStrategy_onExchangeMessage(self, *args)
    def onChessMessage(self, *args): return _cstrat.CStrategy_onChessMessage(self, *args)
    def gateway(self, *args): return _cstrat.CStrategy_gateway(self, *args)
    __swig_destroy__ = _cstrat.delete_CStrategy
    __del__ = lambda self : None;
    def book(self, *args): return _cstrat.CStrategy_book(self, *args)
    def board(self, *args): return _cstrat.CStrategy_board(self, *args)
    def stockfish(self, *args): return _cstrat.CStrategy_stockfish(self, *args)
CStrategy_swigregister = _cstrat.CStrategy_swigregister
CStrategy_swigregister(CStrategy)

class CFactory(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CFactory, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CFactory, name)
    __repr__ = _swig_repr
    __swig_getmethods__["makeStrategy"] = lambda x: _cstrat.CFactory_makeStrategy
    if _newclass:makeStrategy = staticmethod(_cstrat.CFactory_makeStrategy)
    def __init__(self): 
        this = _cstrat.new_CFactory()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cstrat.delete_CFactory
    __del__ = lambda self : None;
CFactory_swigregister = _cstrat.CFactory_swigregister
CFactory_swigregister(CFactory)

def CFactory_makeStrategy(*args):
  return _cstrat.CFactory_makeStrategy(*args)
CFactory_makeStrategy = _cstrat.CFactory_makeStrategy

# This file is compatible with both classic and new-style classes.


