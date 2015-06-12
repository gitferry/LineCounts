import os

class LineCounts(object):
    file_type_list = ['py', 'cpp', 'js', 'c']
    line_counts_dict = {'python': {}, 'c plus plus': {}, 'javaScript': {}, 'c': {}}
    file_type_map = {'py': 'python', 'cpp': 'c plus plus', 'js': 'javaScript', 'c': 'c'}
    file_list = []
    total_counts = 0

    def build_file_list(self, dir = '.'):
        dir_list = os.listdir(dir)
        for name in dir_list:
            path = os.path.join(dir, name)
            if os.path.isdir(path):
                if '.' not in path:
                    self.build_file_list(path)
            else:
                if '.' in path and os.path.basename(path)[0] != '.':
                    file_type = path.split('.')[1]
                    if file_type in self.file_type_list:
                        self.file_list.append(path)

        return self.file_list


    def line_counts(self, dir='.'):
        file_list = self.build_file_list(dir=dir)
        for each_file in file_list:
            lines_number = len(open(each_file).readlines())
            file_name = os.path.basename(each_file)

            file_type = self.file_type_map[each_file.split('.')[1]]
            self.line_counts_dict[file_type][file_name] = lines_number

        print "On the directory of", dir, ", the line number of each file is following:"

        for file_type, file_counts in self.line_counts_dict.iteritems():
            if file_counts:
                print file_type + ":"
                for file_name, line_count in file_counts.items():
                    print file_name + '\t' + str(line_count)
                    self.total_counts += line_count

        print "Total lines of", dir, "is", self.total_counts
        return self.total_counts


if __name__ == "__main__":
    lineCounts = LineCounts()
    lineCounts.line_counts(dir='/Users/keleger/Dropbox/github/lda-adaboost')
