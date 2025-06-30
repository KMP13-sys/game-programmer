import random

# รายชื่อคำศัพท์
words = [ 'python', 'hangman', 'challenge', 'computer', 'programming', 'network', 'security', 'algorithm', 'function', 'variable',
          'syntax' , 'data', 'structure', 'database', 'software', 'hardware', 'internet', 'website', 'application', 'developer', 
          'engineer', 'debugging', 'testing','version', 'control', 'repository', 'framework', 'library', 'module',  'switching',
          'script', 'code', 'editor', 'compiler', 'interpreter', 'runtime', 'exception', 'error', 'bug', 'patch', 
          'update', 'refactor', 'optimization', 'performance', 'scalability', 'usability', 'accessibility', 'interface', 'design', 'architecture', 
          'user', 'experience', 'feedback', 'documentation', 'tutorial', 'guide', 'reference', 'community', 'forum', 'discussion', 
          'collaboration', 'project', 'task', 'issue', 'milestone', 'sprint', 'agile', 'scrum', 'kanban', 'waterfall', 
          'methodology', 'process', 'workflow', 'automation', 'integration', 'deployment', 'cloud', 'virtualization', 'containerization', 'microservices', 
          'api', 'webservice', 'protocol', 'http', 'https', 'tcp', 'udp', 'ip', 'dns', 'ssl', 
          'tls', 'encryption', 'authentication', 'authorization', 'session', 'cookie', 'token', 'csrf', 'xss', 'sql', 
          'injection', 'vulnerability', 'exploit', 'penetration', 'networking', 'audit', 'compliance', 'regulation', 'policy', 'routing',  
          'risk','incident', 'response', 'backup', 'recovery', 'disaster', 'planning',  'monitoring', 'logging', 
          'alerting', 'metrics', 'dashboard', 'visualization', 'analytics', 'bigdata', 'machinelearning', 'artificialintelligence', 'deeplearning', 'neuralnetwork', 
          'dataanalysis', 'datavisualization', 'businessintelligence', 'reporting', 'dashboarding', 'datawarehouse', 'datamining', 'dataengineering', 'datascience', 'statistics', 
          'probability', 'linearalgebra', 'calculus','firewall', 'graph', 'theory', 'combinatorics', 'settheory', 'logic', 'discrete', 
          'mathematics', 'numbertheory', 'cryptography', 'informationtheory', 'complexitytheory',  'computationaltheory', 'algorithmic', 'game', 'decision', 
           'proxy' 'operationsresearch', 'simulation', 'modeling', 'queuing', 'contentdeliverynetwork', 'scheduling', 'inventory', 'management', 
          'supplychain','logistics', 'transportation', 'protocols','vpn', 'loadbalancing', 'caching']

# สุ่มคำ
word = random.choice(words)
guessed_letters = []
tries = 6

# สร้างหน้ากากของคำ
def display_word():
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

print("🎉 ยินดีต้อนรับสู่เกม Hangman!")
print(display_word())

# วนลูปเกม
while tries > 0 and set(word) != set(guessed_letters):
    guess = input("เดาตัวอักษร: ").lower()
    
    if guess in guessed_letters:
        print("คุณเดาไปแล้ว ลองตัวอื่นดูนะ")
    elif guess in word:
        guessed_letters.append(guess)
        print("ถูกต้อง! 😃")
    else:
        guessed_letters.append(guess)
        tries -= 1
        print(f"ไม่ใช่จ้า! เหลือโอกาสอีก {tries} ครั้ง 😢")
    
    print(display_word())

# ผลลัพธ์
if set(word) == set(guessed_letters):
    print("คุณชนะ! 🎉 คำคือ:", word)
else:
    print("คุณแพ้ คำคือ:", word)