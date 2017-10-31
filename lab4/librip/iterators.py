# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ign      ore_case = False

        #assert len(items) > 0
        self.newlst = []
        self.lst = (x for x in items)
        self.ignore_case = kwargs.get('ignore_case', False)







    def __next__(self):
        # Нужно реализовать __next__
        try:
            buf = next(self.lst)
            if self.ignore_case is False and isinstance(buf,str):
                if buf.lower() not in self.newlst:
                    self.newlst.append(buf.lower())
                    return buf
            else:
                if buf not in self.newlst:
                    self.newlst.append(buf)
                    return buf
            return next(self)


        except Exception:
            raise StopIteration()





    def __iter__(self):
        return self
