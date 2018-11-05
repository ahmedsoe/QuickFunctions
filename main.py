# QuickFunctions

# show the NaN rows in a df
nans = lambda df: df[df.isnull().any(axis=1)]
nans(your_df_name_here)

# Print all lines
with pd.option_context('display.max_rows', 50, 'display.max_columns', None):
    display(df) #or print(df)  

# Apply based on other columns
df['YearQuarter'] = df[['Year','Quarter']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)

# Load all df's in a location
path = r'C:/my/path/goes/here' # use your path
all_files = glob.glob(os.path.join(path, "*.csv"))     # advisable to use os.path.join as this makes concatenation OS independent
df_from_each_file = [pd.read_csv(f) for f in all_files]

# Find rows in 1 df not in another df
pd.merge(df1,df2, how='outer', indicator=True) 

#Logging
logging.basicConfig(filename=r"path/to/logfile.log",
                    level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
LOGGER = logging.getLogger('logfilename')
LOGGER.debug('Logger ready')

#Logging2
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

#Logging3
logger = logging.root # WORKS
logger = logging.getLogger('root') # DOES NOT WORK

# Show more numpy
np.set_printoptions(edgeitems=10) 
np.core.arrayprint._line_width = 80 # how long each line is

#Add dash .iplot() to a dataframe
import cufflinks as cf
cf.set_config_file(offline=True, world_readable=False )
df.iplot()

# Remove time from datetime
TODAY = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
