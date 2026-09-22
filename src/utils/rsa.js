/**
 * RSA Cryptography Math Utilities
 */

export function isPrime(number) {
  const num = Number(number);
  if (num < 2) return false;
  if (num === 2) return true;
  if (num % 2 === 0) return false;
  for (let i = 3; i <= Math.sqrt(num); i += 2) {
    if (num % i === 0) return false;
  }
  return true;
}

export function gcd(a, b) {
  let x = Math.abs(a);
  let y = Math.abs(b);
  while (y) {
    const t = y;
    y = x % y;
    x = t;
  }
  return x;
}

export function extendedGcd(a, b) {
  if (a === 0) {
    return { gcd: b, x: 0, y: 1 };
  }
  const { gcd: g, x: x1, y: y1 } = extendedGcd(b % a, a);
  const x = y1 - Math.floor(b / a) * x1;
  const y = x1;
  return { gcd: g, x, y };
}

export function modInverse(e, phi) {
  const { gcd: g, x } = extendedGcd(e, phi);
  if (g !== 1) return null;
  return ((x % phi) + phi) % phi;
}

export function modPow(base, exp, mod) {
  try {
    let b = BigInt(base);
    let e = BigInt(exp);
    let m = BigInt(mod);
    let res = 1n;
    b = b % m;
    while (e > 0n) {
      if (e % 2n === 1n) res = (res * b) % m;
      b = (b * b) % m;
      e = e / 2n;
    }
    return Number(res);
  } catch (err) {
    // Fallback for standard math
    return Math.pow(base, exp) % mod;
  }
}

export function getRSABreakdown(message, e, d, n) {
  if (!message || !e || !d || !n) return { steps: [], error: null };
  const steps = [];

  for (let i = 0; i < message.length; i++) {
    const char = message[i];
    const ascii = char.charCodeAt(0);

    if (ascii >= n) {
      return {
        steps: [],
        error: `Character '${char}' (ASCII ${ascii}) is >= n (${n}). Please choose larger primes (e.g. p=61, q=53).`,
      };
    }

    const cipher = modPow(ascii, e, n);
    const decAscii = modPow(cipher, d, n);
    const decChar = String.fromCharCode(decAscii);

    steps.push({
      index: i,
      char,
      ascii,
      cipher,
      decAscii,
      decChar,
    });
  }

  return { steps, error: null };
}
