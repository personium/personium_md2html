import logging, logging.handlers
import argparse, datetime, re, os, sys
import fnmatch
import pypandoc

# define paths used by this command
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(ROOT_PATH, 'log')

CMD_NAME = os.path.basename(__file__)
LOG_FILENAME = 'personium_md2html.log'

SUPPORTED_LOCALES = ['en', 'ja']
LINK_FILTER = os.path.join(ROOT_PATH, 'convert_link.py')

CURRENT_PATH = os.getcwd()

# Prepare logging mechanism
if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)
logger = logging.getLogger(__name__)
log_file = os.path.join(LOG_PATH, LOG_FILENAME)
handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=1024*1024*10, backupCount=5)
log_fmt = '%(asctime)s %(levelname)s: %(message)s'
log_formatter = logging.Formatter(log_fmt)
handler.setFormatter(log_formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def log_n_notify_user(temp_str):
    print('### %s ###' % temp_str)
    logger.info(temp_str)
    
def log_failure(temp_str):
    print('ERROR: %s' % temp_str)
    logger.error(temp_str)
    
def parse_command():
    temp_msg = 'Convert markdown file(s) to HTML file(s) recursively in a directory where this command is executed.'
    parser = argparse.ArgumentParser(description=temp_msg)    
    
    temp_msg = 'Specify the locale of your github.css.'
    parser.add_argument('--locale', help=temp_msg, choices=SUPPORTED_LOCALES, default="en")
    
    parser.add_argument('--source_dir', default=CURRENT_PATH, help=argparse.SUPPRESS)
    
    parser.set_defaults(func=set_parameters)

    args = parser.parse_args()
    args.func(args)
    
def set_parameters(args):
    source_dir = args.source_dir
    css_path = '/%s/github.css' % args.locale
    
    css_path_option = '-c%s' % css_path
    
    convert_files(source_dir, css_path_option)
    
def convert_files(source_dir, css_path_option):
    log_n_notify_user("Converting markdown to HTML ...")
    for directory, subdirectories, files in os.walk(source_dir):
        for file in fnmatch.filter(files, "*.md"):
            src_name = os.path.join(directory, file)
            src_filename = file.rsplit('.', 1)[0]
            if src_filename == "README":
                target_name = os.path.join(directory, "index.html")
            else:
                target_name = os.path.join(directory, "%s.html" % src_filename)

            output = pypandoc.convert_file(
                source_file=src_name,
                outputfile=target_name,
                to='html',
                format='markdown_github',
                extra_args=(css_path_option, '-s'),
                filters=[LINK_FILTER])
                
            logger.info("Converted from %(src)s to %(dst)s." % { "src": src_name, "dst": target_name })

def main():
    try:
        parse_command()
                
        log_n_notify_user("Successfully converted all the files.")
    except Exception as exc:
        log_failure('Failed to execute %s, reason=%s' % (CMD_NAME, str(exc)))
        exit(1)
            
if __name__ == '__main__':
    main()