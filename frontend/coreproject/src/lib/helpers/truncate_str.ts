export const truncate_str = (str: string, max_legth: number) => {
  return str.length > max_legth ? str.slice(0, max_legth - 4) + ' ...' : str
}