class PythonWriter
  def initialize(out_file)
    @out = File.new(out_file, 'w')
    @indent_level = 0
  end

  # indent increases the tab level by one
  #
  # indent returns the indent level after the increment
  def indent
    @indent_level += 1
  end


  # undent decreases the tab level by one
  #
  # undent returns the indent level after the decrement
  def undent
    @indent_level > 0 ? @indent_level -= 1 : @indent_level = 0
  end
  

  # add_import writes a python import statement to the target file.  
  # You must provide a target, you can also provide an option from value
  def add_import(target, from = nil)
    from.nil? ? write("import #{target}") : write("from #{from} import #{target}")
  end


  # add_print writes a python print statement to the target file.
  # You are required to provide a message, you can also provide a
  # list of variables to be substituted into the message.
  def add_print(message, *subs)
    subs.empty? ? write("print \"#{message}\"") : write("print \"#{message}\" % (#{subs.join ', '})")
  end


  # file_open writes a python open call to the target file.  It takes
  # a filename and mode as arguments.
  def file_open(filename, mode)
    write "open(#{argument_string(filename, mode)})"
  end


  # find_self generates python code that determines the current directory.
  # It takes the name of the variable to put the path into as an argument.
  #
  # find_self returns the generated statement.
  def find_self(path_var)
    "#{path_var} = '/'.join(os.path.realpath(__file__).split('/')[0:-1])"
  end


  # file_close generates a close method call.
  #
  # file_close returns the generated string
  def file_close(token)
    '.close()'
  end


  # write writes the given string to the target file.  It takes a
  # string as an argument.  Write also takes into account the current
  # indent level and modifies the provided string accordingly.
  def write(string)
    @indent_level > 0 ? @out.puts(add_indent string) : @out.puts(string)
    @out.flush
  end


  # add_indent adds spaces to the given string in order to create the
  # proper indent level.  It requires a string and will optionally take
  # a manual indent level.  The default is to use the @indent_level
  # value.
  def add_indent(string, level = @indent_level)
    string.split("\n").each { |line| line.prepend('  ' * level) }.join("\n")
  end


  # for_in writes a for x in y style python statement to the target file.
  # It takes the target collection and an arbitrary number of values as
  # arguments.  If given more than one argument for values it will generate
  # a for x, y, ... in bob style statement.
  def for_in(collection, *values)
    raise("Value Needed.") if values.empty?

    write "for #{values.join(', ')} in #{collection}:"
  end


  # finish closes the target file
  def finish
    @out.close
  end


  private

  # argument_string generates a function argument string from a list of
  # values.  For example argument_string('bob', 'tom', 'sally') will
  # return: "\"bob\", \"tom\", \"sally\""
  def argument_string(*args) # TODO: This assumes all arguments are strings, that's stupid.
    args.join('", "').prepend('"') + '"'
  end
end