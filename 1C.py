def convert(number: str) -> str:
    return '495' + number if len(number) == 7 else number[1:]


def phone(number: str) -> str:
    new_num, *old_nums = number.split('\n')
    new_num = ''.join(i for i in new_num if i.isdigit())
    new_num = convert(new_num)
    result = []
    for old_num in old_nums:
        old_num = ''.join(i for i in old_num if i.isdigit())
        old_num = convert(old_num)
        result.append('YES') if old_num == new_num else result.append('NO')
    return '\n'.join(result)


if __name__ == '__main__':
    assert phone('8(495)430-23-97\n+7-4-9-5-43-023-97\n4-3-0-2-3-9-7\n8-495-430') == 'YES\nYES\nNO'
    assert phone('86406361642\n83341994118\n86406361642\n83341994118') == 'NO\nYES\nNO'
    assert phone('+78047952807\n+78047952807\n+76147514928\n88047952807') == 'YES\nNO\nYES'
