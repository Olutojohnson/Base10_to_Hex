def dec_to_hex(dec_val):
    try:
        if "." in str(dec_val):
            ans = 'Only Integer Values (Non Decimal Values) Are Valid'
            return ans
        elif dec_val == 0:
            return 0
        else:
            ans = []
            while dec_val > 0:
                rem = dec_val % 16
                if rem in range(10, 16):
                    rem_val = {
                        "10": "A",
                        "11": "B",
                        "12": "C",
                        "13": "D",
                        "14": "E",
                        "15": "F"
                    }
                    rem = rem_val.get(str(rem))
                dec_val = dec_val // 16
                ans.append(str(rem))
            ans = ans[::-1]
            return "".join(ans)

    except TypeError:
        ans = 'Invalid Input\nOnly Integer Values Are Valid'
        return ans


print(dec_to_hex(17))
