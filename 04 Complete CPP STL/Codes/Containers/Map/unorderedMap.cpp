#include<iostream>
#include<map>
#include<unordered_map>
using namespace std;

int main(){
    // Creation of unordered_map
    unordered_map<string, string> table;

    // Insertion
    // 1st method: Using the bracket operator
    table["in"] = "India";

    // 2nd method: Using insert() with make_pair()
    table.insert(make_pair("en", "England"));

    // 3rd method: Using pair and insert()
    pair<string, string> p;
    p.first = "br";
    p.second = "Brazil";
    table.insert(p);

    // Size of the unordered_map
    cout << "Size: " << table.size() << endl;

    // Clear all elements from the unordered_map (optional, currently commented out)
    // table.clear();

    // Erase elements (optional, currently commented out)
    // table.erase(table.begin(), table.end());

    // Check if the unordered_map is empty
    if (table.empty()) {
        cout << "Map is empty" << endl;
    } else {
        cout << "Map is not empty" << endl;
    }

    // Accessing elements using at()
    cout << "Value for key 'in': " << table.at("in") << endl;

    // Updating values using at() and bracket operator
    table.at("in") = "Indian";
    table["in"] = "India2";
    cout << "Updated value for key 'in': " << table.at("in") << endl;

    // Iterating through the unordered_map
    unordered_map<string, string>::iterator it = table.begin();
    while (it != table.end()) {
        pair<string, string> p = *it;
        cout << p.first << " -> " << p.second << endl;
        it++;
    }

    // Finding a key using find()
    if (table.find("im") != table.end()) {
        cout << "Key 'im' found" << endl;
    } else {
        cout << "Key 'im' not found" << endl;
    }

    // Counting occurrences of a key using count()
    if (table.count("in") == 0) {
        cout << "Key 'in' not found" << endl;
    } else {
        cout << "Key 'in' found" << endl;
    }

    return 0;
}