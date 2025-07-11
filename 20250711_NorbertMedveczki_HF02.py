"""II. Feladat
Adott az alábbi három lista:
ranges = [class_a_range, class_b_range, class_c_range, class_d_range, class_e_range]
descriptions = [class_a_description, class_b_description, class_c_description,
class_d_description, class_e_description]
class_labels = ["A", "B", "C", "D", "E"]
A listák indexei megegyeznek a hozzájuk tartozó leírással és címkével.
ranges[0] -> descriptions[0] –> class_labels[0]
ranges[1] -> descriptions[1] –> class_labels[1]
…
ranges[n] -> descriptions[n] –> class_labels[n]
1. Dictionary comprehension-el oldd meg, hogy egy alábbi módon meghatározott
dict.-et kapj:
ip_classes = {
"A": {"range": class_a_range, "description": class_a_description},
"B": {"range": class_b_range, "description": class_b_description},
"C": {"range": class_c_range, "description": class_c_description},
"D": {"range": class_d_range, "description": class_d_description},
"E": {"range": class_e_range, "description": class_e_description
}
2. Olvassunk be egy teljes IP címet és írjuk ki, hogy az milyen osztályú cím
3. A felhasználó biztosan jól adja meg, azt nem kell ellenőrizni.
4. A program kommunikációját a mintának megfelelően alakítsd.
"""

"""Here's a simplified overview of the original classes:

Class A: First octet 1-126. Large networks, many hosts.
Class B: First octet 128-191. Medium-sized networks.
Class C: First octet 192-223. Smaller networks.
Class D: First octet 224-239. Used for multicast addressing.
Class E: First octet 240-255. Reserved for experimental purposes."""

def IP_Cim_Ellenorzes(input_ip):
    """init variables"""
    range_tuple = [126, 191, 223, 239, 255]
    description_tuple = ["Class A: First octet 1-126. Large networks, many hosts.", "Class B: First octet 128-191. Medium-sized networks.", "Class C: First octet 192-223. Smaller networks.", "Class D: First octet 224-239. Used for multicast addressing.", "Class E: First octet 240-255. Reserved for experimental purposes."]
    class_labels = []
    ip_classes = {}
    
    """init structures for IP address names handling"""
    for i in range(ord('a'), ord('e') + 1):
        #range_tuple.append(str("class_" + chr(i) + "_range"))
        #description_tuple.append(str("class_" + chr(i) + "_description"))
        class_labels.append(str(chr(i).upper()))
    
    """init dictionary for the IP types"""
    for i in range(len(range_tuple)):
        ip_classes[i] = {class_labels[i] : {"range" : range_tuple[i], "description" : description_tuple[i]}}

    """prepare input data for processing"""
    raw_temp_ip = input_ip.split(".")
    
    """identify class"""
    identified_class = ""
    for i in range(len(range_tuple)):
        #print(raw_temp_ip[0], i)
        if int(raw_temp_ip[0]) <= int(range_tuple[i]):
            identified_class = class_labels[int(i)]
            break
    return (identified_class)


def main():
    print("Egy IP cím osztályát állapítjuk meg.")
    ip_string = input("Adj meg egy teljes IP címet (x.x.x.x/x)")
    print("A megadott IP cím osztálya: ",IP_Cim_Ellenorzes(ip_string))

    return 0

main()