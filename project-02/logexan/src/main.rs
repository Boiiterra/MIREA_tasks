// Данный код преобразует выражения:
// a + b * c
// в подходящие для интерпритации выражения:
// (+ a (* b c))
//
// опираясь на которые, выполняется генерация кода
// и демонстрация таблиц истинности
//
// Данный код основан на одной из статей по Pratt Parsing.
// Пересказывать статью не буду к сожалению, не хватит времени.

use std::env;
use std::fmt;

enum S {
    Atom(char),
    Cons(char, Vec<S>),
}

impl fmt::Display for S {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            S::Atom(i) => write!(f, "{}", i),
            S::Cons(head, rest) => {
                write!(f, "({}", head)?;
                for s in rest {
                    write!(f, " {}", s)?
                }
                write!(f, ")")
            }
        }
    }
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
enum Token {
    Atom(char),
    Op(char),
    Eof,
}

struct Lexer {
    tokens: Vec<Token>,
}

impl Lexer {
    fn new(input: &str) -> Lexer {
        let mut tokens = input
            .chars()
            .filter(|it| !it.is_ascii_whitespace())
            .map(|c| match c {
                '1' | '0' | 'a'..='z' | 'A'..='Z' => Token::Atom(c),
                _ => Token::Op(c),
            })
            .collect::<Vec<_>>();
        tokens.reverse();
        Lexer { tokens }
    }

    fn next(&mut self) -> Token {
        self.tokens.pop().unwrap_or(Token::Eof)
    }
    fn peek(&mut self) -> Token {
        self.tokens.last().copied().unwrap_or(Token::Eof)
    }
}

fn expr(input: &str) -> S {
    let mut lexer = Lexer::new(input);
    expr_bp(&mut lexer, 0)
}

fn expr_bp(lexer: &mut Lexer, min_bp: u8) -> S {
    let mut lhs = match lexer.next() {
        Token::Atom(it) => S::Atom(it),
        Token::Op('(') => {
            let lhs = expr_bp(lexer, 0);
            assert_eq!(lexer.next(), Token::Op(')'));
            lhs
        }
        Token::Op(op) => {
            let ((), r_bp) = prefix_binding_power(op);
            let rhs = expr_bp(lexer, r_bp);
            S::Cons(op, vec![rhs])
        }
        t => panic!("bad token: {:?}", t),
    };

    loop {
        let op = match lexer.peek() {
            Token::Eof => break,
            Token::Op(op) => op,
            t => panic!("bad token: {:?}", t),
        };

        if let Some((l_bp, r_bp)) = infix_binding_power(op) {
            if l_bp < min_bp {
                break;
            }
            lexer.next();

            lhs = if op == '?' {
                let mhs = expr_bp(lexer, 0);
                assert_eq!(lexer.next(), Token::Op(':'));
                let rhs = expr_bp(lexer, r_bp);
                S::Cons(op, vec![lhs, mhs, rhs])
            } else {
                let rhs = expr_bp(lexer, r_bp);
                S::Cons(op, vec![lhs, rhs])
            };
            continue;
        }

        break;
    }

    lhs
}

fn prefix_binding_power(op: char) -> ((), u8) {
    match op {
        '!' => ((), 15),
        _ => panic!("bad op: {:?}", op),
    }
}

fn infix_binding_power(op: char) -> Option<(u8, u8)> {
    let res = match op {
        '-' => (1, 2),   // nor
        '|' => (3, 4),   // nand
        '=' => (5, 6),   // equality
        '.' => (7, 8),   // implication
        '/' => (9, 10),  // xor
        '+' => (11, 12), // or
        '*' => (13, 14), // and
        _ => return None,
    };
    Some(res)
}

#[test]
fn tests() {
    let s = expr("a");
    assert_eq!(s.to_string(), "a");

    let s = expr("a + b * c");
    assert_eq!(s.to_string(), "(+ a (* b c))");

    let s = expr("a + b * c * d + e");
    assert_eq!(s.to_string(), "(+ (+ a (* (* b c) d)) e)");

    let s = expr("f . g . h");
    assert_eq!(s.to_string(), "(. (. f g) h)");

    let s = expr("!a");
    assert_eq!(s.to_string(), "(! a)");

    let s = expr("b + !a");
    assert_eq!(s.to_string(), "(+ b (! a))");

    let s = expr("a = b");
    assert_eq!(s.to_string(), "(= a b)");

    let s = expr("a * b = b");
    assert_eq!(s.to_string(), "(= (* a b) b)");

    let s = expr("!(x . z . (y . z . (x + y . z)))");
    assert_eq!(s.to_string(), "(! (. (. x z) (. (. y z) (. (+ x y) z))))");

    let s = expr("a * b = b / c");
    assert_eq!(s.to_string(), "(= (* a b) (/ b c))");

    let s = expr("f | g . h");
    assert_eq!(s.to_string(), "(| f (. g h))");

    let s = expr("a + b * c - d + e");
    assert_eq!(s.to_string(), "(- (+ a (* b c)) (+ d e))");
}

fn main() {
    let args: Vec<String> = env::args().collect();
    println!("{:?}", args);
    if args.len() == 1 {
        println!("Invalid use of manipulator. Try: {} !a", args[0]);
        return;
    }
    let line = &args[1];

    let s = expr(line);
    println!("{}", s)
}
