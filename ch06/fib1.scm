; Scheme supports tail recursion, no limit on recursive calls
;
; > sudo apt-get install racket  <--- install
; > racket -f fib1.scm           <--- run

(define (fib1 n)
    (define (f a b n)
        (if (= n 0)
            a
            (f b (+ a b) (- n 1))))  ; tail-recursive call
    (f 0 1 n) )

(display (fib1 4000))
(newline)

