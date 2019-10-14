
class ADT(object):
    """
    The class provides basic dictionary-like behaviour.
    Adapted from Christian Kreibich
    """
    def __init__(self, **kwargs):
        # The triplets for each keyword correspond to (1) the actual
        # value, (2) a user-suitable label for the item, and (3) an
        # ordering index:
        self.attrs = {
            'title':         [None, 'Title',          0],
            'year':          [None, 'Year',           1],
            'num_versions':  [0,    'Versions',       2],
        }
        for k,v in kwargs.items():
            self.__setitem__(k, v)

    def __getitem__(self, key):
        if key in self.attrs:
            return self.attrs[key][0]
        return None

    def __len__(self):
        return len(self.attrs)

    def __setitem__(self, key, item):
        if key in self.attrs:
            self.attrs[key][0] = item
        else:
            self.attrs[key] = [item, key, len(self.attrs)]

    def __delitem__(self, key):
        if key in self.attrs:
            del self.attrs[key]

    def as_txt(self):
        # Get attrs sorted in specified order:
        items = sorted(list(self.attrs.values()), key=lambda item: item[2])
        # Find largest label length:
        max_label_len = max([len(str(item[1])) for item in items])
        fmt = '%%%ds %%s' % max_label_len
        res = []
        for item in items:
            if item[0] is not None:
                res.append(fmt % (item[1], item[0]))
        return '\n'.join(res)

    def as_csv(self, header=False, sep='|'):
        # Get keys sorted in specified order:
        keys = [pair[0] for pair in \
                sorted([(key, val[2]) for key, val in list(self.attrs.items())],
                       key=lambda pair: pair[1])]
        res = []
        if header:
            res.append(sep.join(keys))
        res.append(sep.join([unicode(self.attrs[key][0]) for key in keys]))
        return '\n'.join(res)


if __name__ == "__main__":
    x = ADT(title="abc",year=4,num_versions=5)
    x["new"] = "ohohoh"
    print(x.as_txt())
    print(x.as_csv(sep=","))