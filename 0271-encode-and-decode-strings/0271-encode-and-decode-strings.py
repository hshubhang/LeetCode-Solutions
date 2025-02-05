class Codec:
    def encode(self, strs):
        encoded_string = ''

        for s in strs:
            encoded_string += s.replace('/', '//') + '/:'

        return encoded_string

    def decode(self, s):
        decoded_strings = []

        current_string = ""
        i = 0
        while i < len(s):
            if s[i:i+2] == '/:':
                decoded_strings.append(current_string)
                current_string = ""
                i += 2
            elif s[i:i+2] == '//':
                current_string += '/'
                i += 2
            else:
                current_string += s[i]
                i += 1

        return decoded_strings