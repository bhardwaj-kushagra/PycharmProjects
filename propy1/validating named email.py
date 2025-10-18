import email.utils
if __name__ == '__main__':
    n = int(input())
    leProxy = []
    for _ in range(n):
        leProxy.append(list(email.utils.parseaddr(input())))
    def checker(proxy):
        try:
            sep_list = proxy[1].split('@')
            username = sep_list[0]
            domain = sep_list[1].split('.',maxsplit=1)[0]
            extension = sep_list[1].split('.',maxsplit=1)[1]

            for i in range(len(username)):
                if not (username[i].isalnum() or username[i] == '-' or username[i] == '.' or username[i] == '_'):
                    return False

            if not (domain.isalpha() and extension.isalpha() and len(extension) < 4 and len(extension) > 0 and username[0].isalpha()):
                return False
        except IndexError:
            return False

        return True

    leReal = [lEmail for lEmail in leProxy if checker(lEmail)]

    for lItem in leReal:
        print(email.utils.formataddr(lItem))


