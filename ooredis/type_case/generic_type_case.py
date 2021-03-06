# coding: utf-8

from numbers import Integral

class GenericTypeCase:

    """ 
    通用类型转换类，可以处理 str/unicode/int/float 类型值。
    """

    @staticmethod
    def encode(value):
        """ 
        接受 int/long/str/unicode/float 类型值，
        否则抛出 TypeError 。
        """
        if isinstance(value, basestring) or \
           isinstance(value, Integral) or \
           isinstance(value, float):
            return value

        raise TypeError

    @staticmethod
    def decode(value):
        """ 
        将传入值转换成 int/long/str/unicode/float 等格式。
        因为 redis 只返回字符串值，这个函数也只接受字符串值，
        否则抛出 AssertionError 。
        """
        if value is None:
            return
        
        # 以下类型转换规则是基于 Redis 只返回
        # 字符串值这个假设之上来构造的
        # 这里用一个断言来保证这种假设
        assert isinstance(value, basestring)

        # 从最限定的类型开始转换
        try: return int(value)
        except:
            try: return float(value)
            except:
                try: return str(value)
                except:
                    return unicode(value)
