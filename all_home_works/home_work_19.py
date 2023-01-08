class AttributePrinterMixin:
    def __str__(self):
        all_attributes_dict = self.__dict__
        inherit_three = A.__mro__
        list_with_class_names = []
        for i in inherit_three:
            if i.__name__ != 'object':
                list_with_class_names.append(i.__name__)
        all_attributes_updated = {}
        for key, value in all_attributes_dict.items():
            self_class_length = len(self.__class__.__name__)
            if key[0] == '_' and key[1:self_class_length+3] == self.__class__.__name__+'__':
                key = key.replace('_', '', 1)
                key = key.replace(f'{self.__class__.__name__}__', '', 1)
            for name in list_with_class_names:
                len_class_count = len(name)
                if key[0] == '_' and key[1:len_class_count + 1] == name:
                    key = key.replace('_', '', 1)
                    key = key.replace(f'{name}__', '', 1)
            if key[0] == '_' and key[1] != '_':
                key = key.replace(key[0], '', 1)
            all_attributes_updated[key] = value
        print(self.__class__.__name__, ':', ' {', sep='')
        for _ in all_attributes_updated:
            print('    ', _, ': ', all_attributes_updated[_], sep='')
        return '}'


class B:
    def __init__(self):
        self.a1nother_bcls = 1
        self.__2fakenother_bclss = 2
        self.__3another_bclass = 3


class C:
    def __init__(self):
        self.s4 = 54
        self._s5 = [54]
        self.__s6 = 54


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
