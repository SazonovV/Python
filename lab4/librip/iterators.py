# Итератор для удаления дубликатов
class Unique(object):
    lst = []

    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ign      ore_case = False

        #assert len(items) > 0
        self.index = -1
        self.newlst = []
        self.lst = list(items)

        assert len(self.lst)>0
        self.ignore_case = False
        for key in kwargs:
            self.ignore_case = kwargs[key]
        if self.ignore_case == False:
            self.lst.sort(key = lambda x: x.lower())
        else:
            self.lst.sort()
        counter = 0
        self.newlst.append(self.lst[0])
        if self.ignore_case == True:
            for i in self.lst:
                if self.newlst[counter] != i:
                    counter += 1
                    self.newlst.append(i)
        elif self.ignore_case == False:

            for i in self.lst:
                if isinstance(i,str):
                    if self.newlst[counter].lower() != i.lower():
                        counter += 1
                        self.newlst.append(i)
                else:
                    if self.newlst[counter] != i:
                        counter += 1
                        self.newlst.append(i)






    def __next__(self):
        # Нужно реализовать __next__    
        if self.index >= len(self.newlst) - 1:
            raise StopIteration
        self.index += 1
        return self.newlst[self.index]

    def __iter__(self):
        return self
