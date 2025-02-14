T = int(input())


def is_palindrome(start, end, standard, string, is_row=True):
    length = end - start + 1
    tmp_string = string
    for i in range(1, M // 2 + 1):
        ns = start - i
        ne = end + i
        if ns < 0 or ne >= N:
            continue
        if is_row:
            if keyboard[standard][ns] == keyboard[standard][ne]:
                tmp_string = (
                    keyboard[standard][ns] + tmp_string + keyboard[standard][ne]
                )
                length += 2
            else:
                break
        else:
            if keyboard[ns][standard] == keyboard[ne][standard]:
                tmp_string = (
                    keyboard[ns][standard] + tmp_string + keyboard[ne][standard]
                )
                length += 2
            else:
                break
        if M == length:
            break
    return M == length, tmp_string


def solution(N, M, keyboard):
    for i in range(M // 2 - 1, N - 1):
        start = end = i
        for standard in range(N):
            if M % 2:
                tmp_string = keyboard[standard][start]
                is_p, string = is_palindrome(start, end, standard, tmp_string)
                if is_p:
                    return string
                tmp_string = keyboard[start][standard]
                is_p, string = is_palindrome(start, end, standard, tmp_string, False)
                if is_p:
                    return string
            else:
                if keyboard[standard][start] == keyboard[standard][end + 1]:
                    end += 1
                    tmp_string = keyboard[standard][start] + keyboard[standard][end]
                    is_p, string = is_palindrome(start, end, standard, tmp_string)
                    if is_p:
                        return string
                if keyboard[start][standard] == keyboard[end + 1][standard]:
                    end += 1
                    tmp_string = keyboard[start][standard] + keyboard[end][standard]
                    is_p, string = is_palindrome(
                        start, end, standard, tmp_string, False
                    )
                    if is_p:
                        return string


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    keyboard = [input() for _ in range(N)]
    print(f"#{tc} {solution(N, M, keyboard)}")

"""
1
20 13
ECFQBKSYBBOSZQSFBXKI
VBOAIDLYEXYMNGLLIOPP
AIZMTVJBZAWSJEIGAKWB
CABLQKMRFNBINNZSOGNT
NQLMHYUMBOCSZWIOBINM
QJZQPSOMNQELBPLVXNRN
RHMDWPBHDAMWROUFTPYH
FNERUGIFZNLJSSATGFHF
TUIAXPMHFKDLQLNYQBPW
OPIRADJURRDLTDKZGOGA
JHYXHBQTLMMHOOOHMMLT
XXCNJGTXXKUCVOUYNXZR
RMWTQQFHZUIGCJBASNOX
CVODFKWMJSGMFTCSLLWO
EJISQCXLNQHEIXXZSGKG
KGVFJLNNBTVXJLFXPOZA
YUNDJDSSOPRVSLLHGKGZ
OZVTWRYWRFIAIPEYRFFG
ERAPUWPSHHKSWCTBAPXR
FIKQJTQDYLGMMWMEGRUZ
"""
