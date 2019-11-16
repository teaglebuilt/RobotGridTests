from subprocess import check_call


processes = []
print(processes)

for counter in range(1):
    chrome_cmd = 'docker-compose exec robottests scripts/wait_for_it.sh -t 15 selenium_hub:4444 -- robot -A run_chrome.robot'
    firefox_cmd = 'docker-compose exec robottests scripts/wait_for_it.sh -t 15 selenium_hub:4444 -- robot -A run_firefox.robot'
    check_call(chrome_cmd, shell=True)
    check_call(firefox_cmd, shell=True)

    