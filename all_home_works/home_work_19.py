class AttributePrinterMixin:
    def __str__(self):




        test = self.__dict__
        print(test)

        inherit_three = A.__mro__
        massive_with_classes = []
        for i in inherit_three:
            if i.__name__ != 'object':
                massive_with_classes.append(i.__name__)

        result_dict = []
        count = 0
        for i, value in test.items():
            # print('lll', i, value)
            # print(i, value, self.__class__.__name__)
            # add check that this attribute from right class. If not from this class, then user (super function)
# -------------------------for A privated class-------------------------------------
            if i[0] == '_' and i[1:4] == self.__class__.__name__+'__':
                print('11111111111111', i, value)
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

            # if i[0] == '_' and i[1:4] != self.__class__.__name__+'__':
            #     print('11111111111111', i, value)
            #     for _ in massive_with_classes:
            #         len_class_count = len(_)
            #         if i[0] == '_' and i[1:len_class_count+1] == _:
            #             i = i.replace('_', '', 1)
            #             i = i.replace(f'{_}__', '', 1)
# -------------------------for inhereted privated class-------------------------------------
# -------------------------for ALL class for all protected attributes-------------------------------------
            if i[0] == '_' and i[1] != '_':
                i = i.replace(i[0], '', 1)
# -------------------------for ALL class for all protected attributes-------------------------------------

                # s = 0
                # for _ in inherit_three:
                #     s += 1
                #     name_of_class = _.__name__
                #     len_count = len(name_of_class)
                #     if i[0] == '_' and i[1:len_count+1] == name_of_class:
                #         i = i.replace('_', '', 1)
                #         i = i.replace(f'{name_of_class}__', '', 1)

            elif i[0] == '_' and i[1] != '_':
                i = i.replace(i[0], '', 1)
                print('2222222222222', i, value)




            result_dict.append(i + ': ' + str(value))
        print(self.__class__.__name__, ':', ' {', sep='')

        amount_items = len(result_dict)
        for _ in range(amount_items):
            print('    ', result_dict[count])
            if count < amount_items:
                count += 1
        print('}')
        return 'aaaa'


class B:
    def __init__(self):
        self.another_bcls = 1
        self.__fakenother_bclss = 2
        self.__another_bclass = 3


class A(AttributePrinterMixin, B):
    def __init__(self):
        B.__init__(self)
        self.public_filed = 3
        self._protected_field = 'q'
        self.__private_field = [1, 2, 3]
        self.__private__field = [1, 2, 3]
        self._protected_fields = (1, 2, 3)


obj = A()
print(obj)
