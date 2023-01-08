class AttributePrinterMixin:
    def __str__(self):

        test = self.__dict__

        inherit_three = A.__mro__
        massive_with_classes = []
        for i in inherit_three:
            if i.__name__ != 'object':
                massive_with_classes.append(i.__name__)

        value_dict = {}
        # result_dict = {
        #     self.__class__.__name__: value_dict
        # }

        count = 0
        for i, value in test.items():
# -------------------------for A privated class-------------------------------------
            if i[0] == '_' and i[1:4] == self.__class__.__name__+'__':
                i = i.replace('_', '', 1)
                i = i.replace(f'{self.__class__.__name__}__', '', 1)
# -------------------------for A privated class-------------------------------------
# -------------------------for inhereted privated class-------------------------------------
            for _ in massive_with_classes:
                len_class_count = len(_)
                if i[0] == '_' and i[1:len_class_count + 1] == _:
                    i = i.replace('_', '', 1)
                    i = i.replace(f'{_}__', '', 1)
#-------------------------for inhereted privated class-------------------------------------
# -------------------------for ALL class for all protected attributes-------------------------------------
            if i[0] == '_' and i[1] != '_':
                i = i.replace(i[0], '', 1)
# -------------------------for ALL class for all protected attributes-------------------------------------
            value_dict[i] = value
        print(self.__class__.__name__, ':', sep='')

        amount_items = len(value_dict)
        for _ in value_dict:
            print('    ', _, ': ', value_dict[_], sep='')
            # if count < amount_items:
                # count += 1
        print('}')
        return ''


class B:
    def __init__(self):
        self.a1nother_bcls = 1
        self.__2fakenother_bclss = 2
        self.__3another_bclass = 3


class C:
    def __init__(self):
        self.s4 = 54
        self._s5 = [54]
        self.__s6 = (54)


class A(AttributePrinterMixin, B, C):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)
        self.p7ublic_filed = 3
        self._p8rotected_field = 'q'
        self.__p9rivate_field = [1, 2, 3]
        self.__p10rivate__field = [1, 2, 3]
        self._p11rotected_fields = (1, 2, 3)


obj = A()
print(obj)
