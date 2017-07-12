// ========== 1. difference with C ===========
// a. 字符常量
// C++
// sizeof('c') == sizeof(char) == 1
// C
// sizeof('c') == sizeof(int)

// b. 函数原型严格与否
// C++: 下列函数不接受参数
// void func();
// C: 下列函数接受任意数量的参数
// void func();

// c. null的表示
// C++: nullptr
// C: NULL

// d. C的标准头文件
// C++: 添加前缀c,而没有后缀.h
// #include <cstdio>
// C
// #include <stdio.h>

#define version __cplusplus

#include <stdio.h>
#include <string>

// 函数默认参数
void doSomething(int a=1, int b=2) {
  printf("do a=%d, b=%d\n", a, b);
}
// 带默认值的参数必须放在不带默认值的参数之后
// void doSomething2(int a, int b=2, int d=3) {
//   // ...
// }
void testDefaultParam() {
  doSomething();
  doSomething(2);
  doSomething(2, 5);
}

// 命名空间
namespace firstName {
  namespace nested
  {
    void func() {
      printf("nestd\n");
    } 
  }
}

namespace secondName
{
  void func() {
    printf("name\n");
  }
}

void func() {
  printf("global\n");
}

void testNamespace() {
  using namespace secondName;
  // error: is ambiguous
  // func();
  secondName::func();
  firstName::nested::func();
  ::func();
}

void testString() {
  // #include <string>
  std::string myStr = "Hello";
  // string是可变的
  myStr.append(" world");
  myStr += "\n";
  printf("%s", myStr.c_str());
}

// 引用
// 一旦赋予，就不能重新赋，而且不能为null
void testReference() {
  std::string str1 = "I am str1";
  // 创建指向str1的引用
  std::string& refStr = str1;
  
  // 对引用的操作会修改对应的object
  refStr += ",haha";
  printf("content:%s addr:%d\n", refStr.c_str(), &refStr);

  // 引用还是指向原来的对象，只是对象改变
  std::string str2 = "I am str2";
  // same as `str1 = str2`
  refStr = str2;
  printf("str1: %s\n", str1.c_str());
  printf("content:%s addr:%d\n", refStr.c_str(), &refStr); 
}

void testConstReference() {
  std::string str3 = "I won't be modified";
  const std::string& refStr = str3;
  // 用const修饰的指针和引用都不能修改
  // refStr += "(not)";
}

class TempObject {
  public:
    TempObject(int num) {
      this->num = num;
    }
    ~TempObject() {
      printf("TempObject:destroy(%d)\n", num);
    }
  private:
    int num;
};
TempObject tempObjectFunc(int num) {
  TempObject* object = new TempObject(num);
  return *object;
}
TempObject* pointerObjectFunc(int num) {
  return new TempObject(num);
}
void someObject(TempObject& object) {
  printf("call ordinary version\n");
}
// reference to temporary object
void someObject(TempObject&& object) {
  printf("call temp version\n");
}
void testTempObject() {
  tempObjectFunc(0);
  // 两者均在当前函数作用域结束时失效
  TempObject ret = tempObjectFunc(1);
  // error
  // TempObject& refRet = tempObjectFunc(2);
  const TempObject& crefRet = tempObjectFunc(2);

  TempObject* pointerRet = pointerObjectFunc(3);
  printf("wait temp object close\n");

  // move semantics
  TempObject* tempObject = new TempObject(4);
  someObject(*tempObject);
  
  // 使用完后即销毁
  someObject(tempObjectFunc(5));

  printf("wait...");
}

// 可被显式转换
enum ECarTypes: uint8_t {
  Sedan, // 0
  Hatchback, // 1
  SUV = 250, // 250
  Hybrid //255
};
// 不能被显式转换(enum class)
// enum class ECarTypes: uint8_t {
//   Sedan, // 0
//   Hatchback, // 1
//   SUV = 250, // 250
//   Hybrid //255
// };
void writeByteToFile(uint8_t inputValue) {
  printf("%d\n", inputValue);
}
void writePreferredCarTypeToFile(ECarTypes inputCarType) {
  // 显式转换为uint8_t
  writeByteToFile(inputCarType);
}
void testEnum() {
  writePreferredCarTypeToFile(ECarTypes::SUV);
}

// 类声明
class Dog {
  // never put a "using namespace" statement in a header
  // 默认为private
  std::string name;
public:
  // 默认构造方法
  Dog();
  // 声明成员函数
  void setName(const std::string& dogsName);
  // 不改变对象状态的函数应该被标记为const。这允许我们能够通过对象的常引用调用这些方法
  // 内联函数：频繁调用的小函数直接替换成代码
  void bark() const {
    printf("%s barks!\n", name.c_str());
  }
  // virtual说明该方法能被子类进行重写，方法默认是不virtual的
  virtual void print() const;

  // 当对象被删除或者超出作用域时会被调用，因而利用[RAII](http://www.jellythink.com/archives/101)在析构函数中自动释放资源(比如memory、containers、mutexes)，减少代码（将资源等封装成类）
  // 析构函数若不为virtual，则当使用基类引用子类对象时，子类的析构函数不会被调用
  virtual ~Dog();
};

// 类实现
Dog::Dog() {
  printf("A dog has been constructed\n");
}

// 若要修改传入对象，则使用引用；若不修改，则使用常引用
void Dog::setName(const std::string& dogsName) {
  // dogsName.append(" -from China");
  name = dogsName;
}

// virtual关键字只在声明期需要标注
void Dog::print() const {
  printf("Dog is %s\n", name.c_str());
  bark();
}

Dog::~Dog() {
  printf("Bye~Bye\n");
}

// [Difference between private, public, and protected inheritance](https://stackoverflow.com/questions/860339/difference-between-private-public-and-protected-inheritance)
class OwnedDog : public Dog{
public:
  void setOwner(const std::string& dogsOwner);
  
  // override关键字非必须
  void print() const override;

  void testPrivateAccess(const OwnedDog& ownedDog);

private:
  std::string owner;
};

void OwnedDog::setOwner(const std::string& dogsOwner) {
  owner = dogsOwner;
}

void OwnedDog::print() const {
  // call base function
  Dog::print();
  printf("Dog is owned by %s\n", owner.c_str());
}

// 同个类的不同对象之间可以相互访问私有数据，因为C++基于类控制访问(https://stackoverflow.com/questions/6921185/why-do-objects-of-the-same-class-have-access-to-each-others-private-data)
void OwnedDog::testPrivateAccess(const OwnedDog& ownedDog) {
  printf("the other dog owned by %s\n", ownedDog.owner.c_str());
}

void testClass() {
  Dog myDog;
  myDog.setName("Lulu");
  myDog.print();

  OwnedDog oDog;
  oDog.setName("Lulu2");
  oDog.setOwner("Lucy");
  oDog.print();

  OwnedDog nDog;
  nDog.testPrivateAccess(oDog);
}

class Point {
  public:
    int x=0;
    int y=0;

    // 默认构造函数
    Point() {};

    // 初始化成员变量的构造函数
    Point(int a, int b):
      x(a),
      y(b) {}

    Point operator+(const Point& rhs) const;

    // Point& operator+=(const Point& rhs);

    Point operator+=(const Point& rhs);
};

Point Point::operator+(const Point& rhs) const {
  return Point(x+rhs.x, y+rhs.y);
}
// Point& Point::operator+=(const Point& rhs) {
//   x += rhs.x;
//   y += rhs.y;
//   return *this;
// }
Point Point::operator+=(const Point& rhs) {
  x += rhs.x;
  y += rhs.y;
  return Point(x, y);
} 

void testOperator() {
  Point a(1, 1);
  Point b(2, 1);
  Point c = a+b;
  a+=b;
  printf("Point c (%d, %d)", c.x, c.y);
  printf("Point a after (%d, %d)", a.x, a.y);
}

// 模板类
template<class T>
class Box {
  public:
    // During compilation, the compiler actually generates copies of each template with parameters substituted, so the full definition of the class must be present at each invocation. 因此模板类完全在头文件中定义
    void insert(const T& input) {
      printf("has inserted...\n");
    }
};

// 模板方法
template<class T>
void barkOneTime(const T& input) {
  input.bark();
}

// 使用typename的模板方法，一般意义上typename和class可互换。
// template<class T>
template<typename T>
void formCube(const T& input) {
    // 如果使用template<class>，此处编译器不知道T::side是type还是value，编译器会默认当做value。
    // 使用typename关键字显式声明类型，与[文档](https://en.wikipedia.org/wiki/Typename)不符
    typename T::side * p;
}
struct LenData {
  // 定义类型
  typedef int side;
};

// 模板参数不一定是class
template<int Y>
void printMsg() {
  printf("output %d number\n", Y);
}

// Error: 'T' does not name a type
// void Box::insert(const T&) {
//     printf("has inserted...\n");
// }
// The compiler will generate and then type-check every invocation of the template
void testTemplate() {
  Box<int> intBox;
  intBox.insert(100);

  // 模板类也可嵌套
  Box<Box<int> > boxBox;
  boxBox.insert(intBox);

  Dog myDog;
  myDog.setName("Huhu");
  barkOneTime(myDog);
  // also works
  barkOneTime<Dog>(myDog);

  printMsg<100>();

  LenData l;
  formCube(l);
}

#include <exception>
#include <stdexcept>
// [一些异常](http://en.cppreference.com/w/cpp/error/exception)
void testException() {
  try {
    throw std::logic_error("A problem happened\n");
  }
  catch (const std::logic_error& ex) {
    printf("%s", ex.what());
  }
  // 捕获任何异常
  catch(...) {
    printf("unknown exception");
    // rethrow exception
    throw;
  }
}

class Thing {
  public:
    int price;
    Thing(int a): price(a) {}
};
// cannot be class
struct compareFunction {
  bool operator()(const Thing& a, const Thing & b) const {
    return a.price < b.price;
  }
};

#include <map>
void testComparator() {
  std::map<Thing, int, compareFunction> thingMap;
  thingMap[Thing(1)] = 1;
}

#include <vector>
#include <algorithm>
void testLambda() {
  std::vector<int> dog_ids;
  for(int i=0; i<3; i++) {
    dog_ids.push_back(i);
  }
  std::vector<int> dog_weights;
  dog_weights.push_back(30);
  dog_weights.push_back(50);
  dog_weights.push_back(10);
  
  // simplely sort dog_weights
  // std::sort(dog_weights.begin(), dog_weights.end(),
  //     [](const int& lhs, const int& rhs) {
  //       return lhs < rhs;
  //     });
  // for(auto weight : dog_weights)
  //   printf("%d-", weight);
  // printf("\n");
  
  // sort dog_id according to dog_weights
  std::sort(dog_ids.begin(), dog_ids.end(),
      [dog_weights](const int& lhs, const int& rhs) {
        return dog_weights[lhs] < dog_weights[rhs];
      });
  // auto作[自动类型推导](http://zh.cppreference.com/w/cpp/language/auto)
  for(auto id : dog_ids)
    printf("%d-", id);
  printf("\n");

  // lambda syntax 
  // [] in the lambda is used to "capture" variables
  // The "Capture List" defines what from the outside of the lambda should be available inside the function body and how.
  // It can be either:
  //     1. a value : [x]
  //     2. a reference : [&x]
  //     3. any variable currently in scope by reference [&]
  //     4. same as 3, but by value [=]
  // see more: http://stackoverflow.com/questions/7627098/what-is-a-lambda-expression-in-c11
}

void testMagicStuff() {
  // 重写私有方法
  class Base {
    virtual void method();
  };
  class Sub : public Base {
    virtual void method();
  };

  class Copy {
    public:
      Copy(){}
      // 实现拷贝构造函数进行深拷贝，避免默认的浅拷贝造成如下现象：
      // 1. b是a的副本，a中成员变量动态开辟堆内存，浅拷贝b也指向同块内存，当a析构后，b中的指针就是野指针
      Copy(const Copy&) {
        printf("call copy method\n");
      }
  };
  Copy c1;
  Copy c2 = c1;

}

#include <tuple>
void testTuple() {
  auto firstTuple = std::make_tuple(10, 'A');
  int size = std::tuple_size<decltype(firstTuple)>::value;
  printf("%d %c %d\n", std::get<0>(firstTuple), std::get<1>(firstTuple), size);
  // 或者这样创建tuple
  std::tuple<int, char> secondTuple(10, 'A');

  // 合并tuple
  auto concat_tuple = std::tuple_cat(firstTuple, secondTuple);
  printf("%d %d\n", std::get<0>(concat_tuple), std::get<2>(concat_tuple));

  // 解包
  int first_num;
  char first_char;
  std::tie(first_num, first_char) = firstTuple;
  printf("%d %c\n", first_num, first_char);
}
int main() {
  testDefaultParam();
  
  testNamespace();
  
  testString();

  testReference();

  testConstReference();

  testTempObject();

  testEnum();

  testClass();

  testOperator();

  testTemplate();

  testException();

  testComparator();

  testLambda();

  testMagicStuff();

  testTuple();

  printf("%d", version);
}

