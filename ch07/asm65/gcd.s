; GCD using Euclid's algorithm: gcd(248,40) = 8
; RTK, 14-Jan-2023

a       equ $0300
b       equ $0301

        org $0302

; Setup, a=248, b=40
        ldx #$f8
        stx a
        ldx #$28
        stx b

; Loop until a=b
loop    lda a
        cmp b
        beq done
        bcc less

; a>b
        lda a
        sec
        sbc b
        sta a
        jmp loop

; a<b
less    lda b
        sec
        sbc a
        sta b
        jmp loop

; Done, gcd in a
done    rts

